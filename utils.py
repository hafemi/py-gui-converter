from __future__ import division
from pyparsing import (Literal, CaselessLiteral, Word, Combine, Group, Optional,
                       ZeroOrMore, Forward, nums, alphas, oneOf)
from PIL import Image
import math
import operator
import conversion_factors as cf
import ntpath
import os


class NumericStringParser(object):
    def pushFirst(self, strg, loc, toks):
        self.exprStack.append(toks[0])

    def pushUMinus(self, strg, loc, toks):
        if toks and toks[0] == '-':
            self.exprStack.append('unary -')

    def __init__(self):
        point = Literal(".")
        e = CaselessLiteral("E")
        fnumber = Combine(Word("+-" + nums, nums) +
                          Optional(point + Optional(Word(nums))) +
                          Optional(e + Word("+-" + nums, nums)))
        ident = Word(alphas, alphas + nums + "_$")
        plus = Literal("+")
        minus = Literal("-")
        mult = Literal("*")
        div = Literal("/")
        lpar = Literal("(").suppress()
        rpar = Literal(")").suppress()
        addop = plus | minus
        multop = mult | div
        expop = Literal("^")
        pi = CaselessLiteral("PI")
        expr = Forward()
        atom = ((Optional(oneOf("- +")) +
                 (ident + lpar + expr + rpar | pi | e | fnumber).setParseAction(self.pushFirst))
                | Optional(oneOf("- +")) + Group(lpar + expr + rpar)
                ).setParseAction(self.pushUMinus)
        factor = Forward()
        factor << atom + \
            ZeroOrMore((expop + factor).setParseAction(self.pushFirst))
        term = factor + \
            ZeroOrMore((multop + factor).setParseAction(self.pushFirst))
        expr << term + \
            ZeroOrMore((addop + term).setParseAction(self.pushFirst))
        self.bnf = expr
        epsilon = 1e-12
        self.opn = {"+": operator.add,
                    "-": operator.sub,
                    "*": operator.mul,
                    "/": operator.truediv,
                    "^": operator.pow}
        self.fn = {"sin": math.sin,
                   "cos": math.cos,
                   "tan": math.tan,
                   "exp": math.exp,
                   "abs": abs,
                   "trunc": lambda a: int(a),
                   "round": round,
                   "sgn": lambda a: abs(a) > epsilon}

    def evaluateStack(self, s):
        op = s.pop()
        if op == 'unary -':
            return -self.evaluateStack(s)
        if op in "+-*/^":
            op2 = self.evaluateStack(s)
            op1 = self.evaluateStack(s)
            return self.opn[op](op1, op2)
        elif op == "PI":
            return math.pi  # 3.1415926535
        elif op == "E":
            return math.e  # 2.718281828
        elif op in self.fn:
            return self.fn[op](self.evaluateStack(s))
        elif op[0].isalpha():
            return 0
        else:
            return float(op)

    def eval(self, num_string, parseAll=True):
        self.exprStack = []
        results = self.bnf.parseString(num_string, parseAll)
        val = self.evaluateStack(self.exprStack[:])
        return val


class UnitConversions:
    def __init__(self):
        self.empty = []
        self.weight = ['Gram', 'Kilogram', 'Pound', 'Ounce', 'Ton']
        self.length = ['Millimeter', 'Centimeter', 'Meter',
                       'Kilometer', 'Inch', 'Foot', 'Yard', 'Mile']
        self.temperature = ['Celsius', 'Fahrenheit', 'Kelvin']
        self.time = ['Second', 'Minute', 'Hour',
                     'Day', 'Week', 'Month', 'Year']
        self.bytes = ['Bit', 'Byte', 'Kilobyte',
                      'Megabyte', 'Gigabyte', 'Terabyte', 'Petabyte']
        self.speed = ['Meter/Second', 'Kilometer/Hour', 'Mile/Hour']
        self.volume = ['Milliliter', 'Liter', 'Gallon',
                       'Cubic Inch', 'Cubic Foot', 'Cubic Meter']
        self.area = ['Sq. Meter', 'Sq. Kilometer', 'Sq. Mile',
                     'Sq. Yard', 'Sq. Foot', 'Acre', 'Hectare']
        self.energy = ['Joule', 'Calorie', 'Kilocalorie',
                       'Kilowatt Hour', 'Electron Volt', 'BTU', 'Foot-Pound']


unit_conv = UnitConversions()
unit_conversions_dict = {
    '': unit_conv.empty,
    'Length': unit_conv.length,
    'Temperature': unit_conv.temperature,
    'Weight': unit_conv.weight,
    'Time': unit_conv.time,
    'Bytes': unit_conv.bytes,
    'Speed': unit_conv.speed,
    'Volume': unit_conv.volume,
    'Area': unit_conv.area,
    'Energy': unit_conv.energy
}


def get_conversionlist(event):
    conversion_list = unit_conversions_dict[event]
    return conversion_list


def calculate_results(values, window):
    nsp = NumericStringParser()
    source_unit = values['-SOURCE_UNIT-'].lower()
    target_unit = values['-TARGET_UNIT-'].lower()
    number = values['-CONVERSION_INPUT-']

    title = window['-TITLE-'].Get()
    selected_unit = title.replace('Convert ', '').lower()

    dict_formula = cf.conversion_factor[selected_unit]  [source_unit][target_unit]
    formula = dict_formula.replace('x', str(number))
    result = nsp.eval(formula)

    return dict_formula, result


def validate_inputs(window, values):
    if 'Converter' in window['-TITLE-'].Get():
        return 'Choose a Unit'
    if values['-CONVERSION_INPUT-'] != '':
        if values['-SOURCE_UNIT-'] == '':
            return 'Select the Unit you want to convert from'
        if values['-TARGET_UNIT-'] == '':
            return 'Select the Unit you want to convert to'
        if values['-SOURCE_UNIT-'] == values['-TARGET_UNIT-']:
            return 'You can not use the same Unit twice'
    return ''


def update_windows(window, event):
    event = event.replace('-', '').capitalize()
    window['-TITLE-'].update(value=f'Convert {event}')
    window['-SOURCE_UNIT-'].update(values=get_conversionlist(event))
    window['-TARGET_UNIT-'].update(values=get_conversionlist(event))
    window['-CONVERSION_RESULT-'].update(value='')
    window['-CONVERSION_INPUT-'].update(value='')
    window['-CONVERSION_FORMULA-'].update(value='Formula: ')
    window['-CONVERSION_ERROR-'].update(value='')


def manage_unit_converter(event, values, window):
    units = ['Length', 'Temperature', 'Weight', 'Time',
             'Bytes', 'Speed', 'Volume', 'Area', 'Energy']
    if event.replace('-', '').capitalize() in units:
        update_windows(window, event)
    if event == '-CONVERSION_INPUT-':
        if values['-CONVERSION_INPUT-'].isdigit():
            error_message = validate_inputs(window, values)
            window['-CONVERSION_ERROR-'].update(value=error_message)
            if error_message == '':
                dict_formula, result = calculate_results(values, window)
                window['-CONVERSION_FORMULA-'].update(value=dict_formula)
                window['-CONVERSION_RESULT-'].update(value=(round(result, 5)))

        else:
            window['-CONVERSION_INPUT-'].update(
                values['-CONVERSION_INPUT-'][:-1])


def get_image_name(values, window):
    image = Image.open(values['-IMAGE_PATH-'])
    image_name = ntpath.basename(image.filename)
    window['-IMAGE_NAME-'].update(value=image_name)

def get_folder_name(values, window):
    folder = values['-FOLDER_PATH-']
    folder_name = os.path.basename(folder)
    window['-FOLDER_NAME-'].update(value=folder_name)

def manage_tab_converter(event, values, window):
    if event == '-IMAGE_PATH-':
        window['-UNITS_TAB-'].update(disabled=True)
        get_image_name(values, window)
    if event == '-FOLDER_PATH-':
        get_folder_name(values, window)
    if event == '-CONVERT_IMAGE-':
        image = Image.open(values['-IMAGE_PATH-'])
        image.save(format=values['-FORMAT_COMBO-'], fp='a')