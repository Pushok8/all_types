#!usr/bin/env python
# -*- coding: UTF-8 -*-
"""                                              All types modulo.
This modulo contains class AllTypes and OnlySelfType descriptor. Almost all magic methods are present in the AllTypes
 class, which means that you can interact with Python literals with an instance of this class. How many class instances
 can be made. You can do this only once, and by default you can make as many instances of the class as you like. More
 detailed documentation is written in the class itself.
"""

from typing import Any, AnyStr, NewType, List, Callable, Dict, Tuple, Set, FrozenSet, TypeVar, Literal, Iterator, IO

__all__ = ['AllTypes', 'OnlySelfType']
__author__ = '©Pushok8'

# Annotation
BuiltInTypes = TypeVar('BuiltInTypes', bool, int, float, complex, str, list, tuple, dict, set, frozenset)
Numbers = TypeVar('Numbers', bool, int, float, complex)
CodeTemplate = NewType('CodeTemplate', str)
NumOrSet = TypeVar('NumOrSet', Numbers, set, frozenset)
ClassInstance = NewType('ClassInsatnce', type)
NumWithoutComplexOrSet = TypeVar('NumbersWithoutComplexOrSet', bool, int, float, set, frozenset)
IntString = NewType('IntString', (int, str))
FileObj = NewType('FileObj', IO)


class OnlySelfType:
    """Descriptor for static variable type at class."""
    def __init__(self, self_type: type) -> None:
        self.__self_type: type = self_type

    def __set_name__(self, owner, name: str) -> None:
        self.__name = name

    def __get__(self, instance, owner) -> Any:
        return self.__self_type(instance.__dict__[self.__name])

    def __set__(self, instance, value: Any) -> None:
        instance.__dict__[self.__name] = self.__self_type(value)

    def __delete__(self, instance) -> None:
        del instance.__dict__[self.__name]


class AllTypes(object):
    """
    The AllTypes class, upon initialization, accepts all the built-in Python3.X data types of the CPython
    implementation (bool, int, float, complex, str, list, tuple, dict, set, frozenset). The data must be specified
    by name in this sequence, because a TypeError error may occur because the object cannot be converted to another
    type. This class implements almost all magic methods and therefore you can interact with an instance using literals.

    Initialization:
     There are two ways:
      First option -> instance = AllTypes(boolean=False, integer=0, float_num=0.0, complex_num=0j, string='', array=[],
                                          tuple_=(,), dictionary={}, set_=set(), frozenset_=frozenset())
      Second option -> instance = AllTypes.define_max_instance(max_instance, [, *args[, **kwargs]])

     Parameters of the first option:
       boolean: any object convertible to boolean.
       integer: any object convertible to integer.
       float_num: any object convertible to float.
       complex_num: any object convertible to complex.
       string: any object convertible to string.
       array: any object convertible to list.
       tuple_: any object convertible to tuple.
       dictionary: any object convertible to dictionary.
       set_: any object convertible to set.
       frozenset_: any object convertible to frozenset.

     Parameters of the second option:
       max_instance: maximum number of class instances.
       args: all parameters specified in the first embodiment.
       kwargs: all named parameters specified in the first variant.

     Class attributes:
       all_types: return tuple all built-in types. (boolean, integer, float_num, complex_num, string, array, tuple_,
                                                    dictionary, set_, frozenset_)
     In the first version, the class with the specified parameters is simply initialized. The second option determines
      how many instances of the class can be made. You can do this only once! By default, you can make as many instances
      of the class as you like.

    Class parameter:
      all_types - all built-in instance types of a class. (boolean, integer, float_num, complex_num, string, array,
                                                                tuple_, dictionary, set_, frozenset_)

    For examples, create an instance.
    obj = AllTypes (False, 4, -2.5, (3-2j), 'sing', [1, 4], (6, 1), {5: '5'}, {1, 6}, frozenset([12, 5]))

    Important! when using instance literals with a complex, the complex must be in brackets otherwise a TypeError error.
        obj + (2-4j) <- Correct
        obj + 2-4j <- Wrong

    Comparisons:
     obj (==, !=) other ->
        is bool or str: each built-in types is converted to a bool or str value and compared with the
          other object. Example - obj == True # (False, True, True, True, True, True, True, True, True, True)
        is int or float: boolean, integer and float_num translate to int or float and compared with the other object.
          Example - obj == 4 # (False, True, False)
        is complex: boolean, integer, float_num and complex_num translate to complex and compare with the other object.
          Example - obj == (4+0j) # (False, True, False, False)
        is dict: compare dict with dictionary. Example - obj != {5: ''} # (True,)
        is list or tuple or set or frozenset: each initialization parameter is converted to a list value
          (25 -> [25], (1, 2, 3) -> {1, 2, 3}, 'str' -> ('s', 't', 'r')) and compared with the other object.
          Example - obj != (1, 2) # (True, True, True, True, True, True, True, True, True, True)
        is other type: tries to compare with all built-in types; if that fails, throws a TypeError.

    obj (<, <=, >=, >) other ->
      Everything is almost the same as when comparing with '==' and '! =', but with a few exceptions.
      if other is list or tuple:
        Trying to compare with all built-in types. If it fails, replaces the boolean value 'Does not compare!'.
        is complex or dict: will return a tuple filled with the string 'Does not compare!'.

    When comparing, a tuple is returned whose length depends on what is being compared.


    Arithmetic operations:
     Those types that are not specified in the enumeration of behavior of type other with an instance are not supported.
     obj + other ->
       is bool or str: each built-in types is converted to a bool or str value and add up with other. Examples -
         obj + True # (1, 2, 2, 2, 2, 2, 2, 2, 2, 2)
         obj + ' + str' # ('False + str', '4 + str', '-2.5 + str', '(3-2j) + str', 'sing + str', '[2, 4] + str',
                           '(6, 1) + str', "{5: '5'} + str", "{'g', 'e'} + str", 'frozenset({6, 12}) + str')
       is int or float or complex: boolean, integer, float_num and complex_num translate to int or float or complex type
         and are added. Examples -
           obj + 4 # (4, 8, 1.5, (7-2j))
           obj + (2-3j) # ((2-3j), (6-3j), (-0.5-3j), (5-5j))
       is list or tuple or set or frozenset: each built-in type is translated into list or tuple or set or frozenset
         (6.2 -> [6.2], 'str' -> ('s', 't', 'r'), {1: 2, 3: 4} -> {1, 3}) and develops. Examples -
         obj + [1, 2] # ([False, 1, 2], [4, 1, 2], [-2.5, 1, 2], [(3-2j), 1, 2], ['s' , 'i', 'n', 'g', 1, 2],
                         [1, 4, 1, 2], [6, 1, 1, 2], [5, 1, 2], [1, 6 , 1, 2], [12, 5, 1, 2])
     other + obj ->
       is bool or str: other with each built-in type are converted to type bool or str and add up. Example -
         '!' + obj # ('!False', '!4', '!-2.5', '!(3-2j)', '!sing', '![1, 4]', '!(6, 1)', "!{5: '5'}", '!{1, 6}',
                      '!frozenset({12, 5})')
       is int or float or complex: other stacks with boolean, integer, float_num and complex_num. Example -
         3 + obj # (3, 7, 0.5, (6-2j))
       is list or tuple or set or frozenset: other stacks with all the built-in types translated into list or tuple or
         set or frozenset. Example - [1, 2] + obj # ([1, 2, False], [1, 2, 4], [1, 2, -2.5], [1, 2, (3-2j)],
                                                     [1, 2, 's', 'i', 'n', 'g'], [1, 2, 1, 4], [1, 2, 6, 1], [1, 2, 5],
                                                     [1, 2, 1, 6], [1, 2, 12, 5])
     obj += other ->
       is bool or int or float: boolean, integer, float_num, complex_num is equal to the result of addition with other.
       is str or list or tuple or dict or set or frozenset: str, array, tuple_, dictionary, set_ and frozenset_ is equal
         to the result of addition with other, converted to the type with which it is added.

     obj - other ->
       is bool or int or float or complex: from boolean, integer, float_num and complex_num is subtracted by other.
         Example - obj - 1.4 # (-1.4, 2.6, -3.9, (1.6-2j))
       is set or frozenset: each built-in types is converted to a set or frozenset value and add up with other.
         ((3-2j) -> {(3-2j)}, 'st' -> {'s', 't'}, [1, 2] -> {1, 2}). Example -
         obj - {1, 2} # ({False}, {4}, {-2.5}, {(3-2j)}, {'i', 'g', 's', 'n'}, {4}, {6}, {5}, {6}, {12, 5})
     other - obj ->
       is bool or int or float or complex: boolean, integer, float_num and complex_num are subtracted from other.
         Example - 2 - obj # (2, -2, 4.5, (-1 + 2j))
       is set or frozenset: subtracted from other all built-in types converted to set or frozenset. Example -
         {4, 2.5} - obj # ({2.5, 4}, {2.5}, {2.5, 4}, {2.5, 4}, {2.5, 4}, {2.5}, {2.5, 4}, {2.5, 4}, {2.5, 4}, {2.5, 4})
     obj -= other ->
       is bool or int or float: boolean, integer, float_num, complex_num are equal to the result of subtracting other.
       is set or frozenset: set and frozenset are equal to the result of subtracting other.

     obj * other ->
       is float or complex: multiply boolean, integer, float_num and complex_num by other. Example -
         obj * 2.5 # (0.0, 10.0, -6.25, (7.5-5j))
       is bool or int : boolean, integer, float_num, complex_num, string, array and tuple_ are multiplied on other.
        Example - obj * 2 # (0, 8, -5.0, (6-4j), 'singsing', [1, 4, 1, 4], (6, 1, 6, 1))
     other * obj ->
       is bool or int or float or complex: other multiply on boolean, integer, float_num and complex_num. Example -
         2 * obj # (0, 8, -5.0, (6-4j))
       is str or list or tuple: other multiply on boolean and integer. Example - 'str' * obj # ('', 'strstrstrstr')
     obj *= other ->
       is bool or int: boolean, integer, float_num, complex_num, string, array and tuple_ equals the result of
         multiplying by other.
       is float: boolean, integer, float_num and complex equals the result of multiplying by other.

     obj / other ->
       is bool or int or float or complex: boolean, integer, float_num and complex_num is divided into other. Example -
         obj / (1-0j) # (0j, (4+0j), (-2.5+0j), (3-2j))
     other / obj ->
       is bool or int or float or complex: other divided on boolean, integer, float_num and complex. Example -
         Note: replaced boolean with True as ZeroDivisionError raises.
         10 / obj # (10.0, 2.5, -4.0, (2.307692307692308+1.5384615384615383j))
     obj /= other ->
       is bool or int or float or complex: boolean, integer, float_num and complex_num is equal to the result of
         division by other.

     obj (//, %) other ->
       is bool or int or float: boolean, integer and float are divided integer or modulo by other. Example -
         obj // 2 # (0, 2, -2.0)
     other (//, %) obj ->
       is bool or int or float: other divided integer or modulo by boolean, integer and float. Example -
         Note: replaced boolean with True as ZeroDivisionError raises.
         10 % obj # (0, 2, -0.0)
     obj (//, %)= other ->
       is bool or int or float: boolean, integer and float is equal to the result of an integer division operation or
         modulo by other.

     obj ** other ->
       is bool or int or float or complex: boolean, integer, float_num, complex are raised to the power of other.
        Example - obj ** True # (0, 4, -2.5, (3-2j))
     other ** obj ->
       is bool or int or float or complex: other is raised to the power of boolean, integer, float_num and complex_num.
         Example - True ** obj # (1, 1, 1.0, (1+0j))
     obj **= other ->
       is bool or int or float or complex: boolean, integer, float_num, complex_num is equal to the result of raising to
         the power of other.

     pow(obj, other, modulo) ->
       other is bool or int or float and modulo is None: boolean, integer, float_num, complex are raised to the power
         of other. Example - pow(obj, 2) # (0, 16, 6.25, (5-12j))
       other is bool or int or float and modulo is bool or int: boolean, integer and float are raised to the power of
         other and are divided modulo. Example - pow(obj, 2, 3) # (0, 1, 1)
     pow(other, obj) ->
       is bool or int or float or complex: other is raised to the power of boolean, integer, float_num and complex_num.
         Example - pow(2, obj) # (1, 16, 0.1767766952966369, (1.4676557979464138-7.86422192328995j))

     divmod(obj, other) ->
       is bool or int or float: boolean, integer and float_num divided integer and modulo. Example -
        divmod(obj, -2) # ((0, 0), (-2, 0), (1.0, -0.5))
     divmod(other, obj) ->
       is bool or int or float: other is divided integer and modulo by boolean, integer and float_num. Example -
        Note: replaced boolean with True as ZeroDivisionError raises.
        divmod(-2, obj) # ((-2, 0), (-1, 2), (0.0, -2.0))

     obj (<<, >>) other ->
       is bool or int: boolean, integer and float binary shift left or right by other. Example - obj >> 5 # (0, 0, -1)
     other (<<, >>) obj ->
       is bool or int: other binary shifts left or right by boolean, integer and float_num. If some value is less than
         zero, inserts 'value < 0'. Example - 3 >> obj # (3, 0, '-2.5 < 0')
     obj (>>, <<)= other ->
       is bool or int: boolean, integer, and float_num equals the result of a binary offset left or right by other.

     obj (&, |, ^) other ->
       is bool or int: boolean, integer and float_num are converted to int and perform the binary operation & or | or ^
         with other. Example - obj ^ 2 # (-2, -2, -2)
       is set or frozenset: each built-in type translated to set or frozenset (25 -> {25}, 'sst' -> {'s', 't'}) and
        perform the operation & or | or ^ with other. Example -
        obj ^ {1, 2} # ({False, 1, 2}, {1, 2, 4}, {1, 2, -2.5}, {1, 2, (3-2j)}, {1, 2, 'n', 's', 'g', 'i'}, {2, 4},
                        {2, 6}, {1, 2, 5}, {2, 6}, {1, 2, 12, 5})
     other (&, |, ^) ->
       is bool or int: other with boolean, integer and float_num perform the binary operation & or | or ^.  Example -
         2 ^ obj # (2, 6, -4)
       is set or frozenset: other with each built-in type translated to set or frozenset perform the operation
         & or | or ^. Example - {1, 2} & obj # (set(), set(), set(), set(), set(), {1}, {1}, set(), {1}, set())
     obj (&, |, ^)= other ->
       is bool or int: boolean, integer and float num are equal to the result of binary operations & or | or ^
         with other.
       is set or frozenset: set and frozenset are equal to the result of the operation & or | or ^ with other.


    Unary operators and functions:
      +obj -> +boolean, +integer, +float_num, +complex_num
      -obj -> -boolean, -integer, -float_num, -complex_num
      abs(obj) -> abs(integer), abs(float_num), abs(complex_num)
      round(obj, 2) -> round(float_num, 2)
      floor(obj) -> floor(float_num)
      ceil(obj) -> ceil(float_num)
      trunc(obj) -> trunc(float_num)

    Transfer functions to another type:
      int (), float (), complex () tried convert string to self type, if it turns out, returns the translated string.
      int(obj) -> int(float_num)
      float(obj) -> float(integer)
      complex(obj) -> complex(integer, float_num)
      bool(obj) -> if at least one element is True in all_types, returns True, if all elements converted to a boolean
                   value are False, returns False
      str(obj) -> '<class (class name) instance at (instance hex id)>'
      repr(obj) -> str(obj)
      list(obj) -> list(all_types)
      hash(obj) -> returns a hash of a tuple in which all hashable types.
      len(obj) -> len(all_types)
      (1, 2, 3)[obj] -> (1, 2, 3)[integer]
      '->{}<-'.format(obj) -> '->{}<-'.format(string)
      obj[2] -> all_types[2]
      iter(obj) -> iter(all_types)
      reversed(obj) -> all_types[::-1]
      2 in obj -> 2 in all_types
      obj() -> If the user has added the called object(s), all called objects are called and all parameters that are
               specified when the instance is called are passed. A dictionary is returned with the name of the called
               object and the value that it returns.

    Context manager: looks for an object that has the attribute "close", and returns a list of these objects.
    """
    from math import floor, ceil, trunc
    from copy import deepcopy

    _max_val_is_changed: bool = False
    _max_quantity_instance: int = -1
    _last_instance: ClassInstance = None

    @classmethod
    def define_max_instance(cls, max_instance: int, *args: BuiltInTypes, **kwargs: BuiltInTypes) -> ClassInstance:
        """Define max quantity instance from class."""
        if cls._max_val_is_changed:
            return 'The maximum number of class instances has already been changed.'
        else:
            cls._max_val_is_changed = True
            cls._max_quantity_instance: int = int(max_instance)
            return cls(*args, **kwargs)

    def __new__(cls, *args: BuiltInTypes, **kwargs: BuiltInTypes) -> _last_instance:
        if cls._max_quantity_instance != 0:
            cls._max_quantity_instance -= 1
            cls._last_instance = super().__new__(cls)
        return cls._last_instance

    # So that the user could not put another type in place of the desired one.
    boolean: bool = OnlySelfType(bool)
    integer: int = OnlySelfType(int)
    float_num: float = OnlySelfType(float)
    complex_num: complex = OnlySelfType(complex)
    string: AnyStr = OnlySelfType(str)
    array: List[Any] = OnlySelfType(list)
    tuple_: Tuple[Any] = OnlySelfType(tuple)
    dictionary: Dict[Any, Any] = OnlySelfType(dict)
    set_: Set[Any] = OnlySelfType(set)
    frozenset_: FrozenSet[Any] = OnlySelfType(frozenset)

    def __init__(self, boolean: bool = bool(), integer: int = int(), float_num: float = float(),
                 complex_num: complex = complex(), string: AnyStr = str(), array: List[Any] = [],
                 tuple_: Tuple[Any] = tuple(), dictionary: Dict[Any, Any] = dict(), set_: Set[Any] = set(),
                 frozenset_: FrozenSet[Any] = frozenset()) -> None:
        self.boolean = boolean
        self.integer = integer
        self.float_num = float_num
        self.complex_num = complex_num
        self.string = string
        self.array = array
        self.tuple_ = tuple_
        self.dictionary = dictionary
        self.set_ = set_
        self.frozenset_ = frozenset_

    # Two "all_types" are created so that if the user changes the public "all_types" there are no bugs.
    @property
    def all_types(self) -> Tuple[BuiltInTypes]:
        return (self.boolean, self.integer, self.float_num, self.complex_num, self.string, self.array, self.tuple_,
                self.dictionary, self.set_, self.frozenset_)

    @property
    def _all_types(self) -> Tuple[BuiltInTypes]:
        return (self.boolean, self.integer, self.float_num, self.complex_num, self.string, self.array, self.tuple_,
                self.dictionary, self.set_, self.frozenset_)

    def _comparison(self, other: Any, compare: Literal = '==') -> Tuple[bool]:
        if compare != '==' and compare != '!=' and compare != '>' and compare != '<' and compare != '>=' and \
                compare != '<=':
            raise NameError("Сompare must be literal!")

        result: List[bool] = []
        numbers: Tuple[Numbers] = (self.boolean, self.integer, self.float_num, self.complex_num)
        type_numbers: Tuple[Numbers] = tuple(map(type, numbers))
        type_other: type = type(
            other)  # It is done in order not to write a strange construct, for example: type(other)(val)
        type_all_types: Tuple[BuiltInTypes] = tuple(map(type, self._all_types))
        if isinstance(other, (bool, str)) or type_other not in type_all_types:
            for val in self._all_types:
                try:
                    result.append(eval(f'type_other(val) {compare} other'))
                except (TypeError, SyntaxError):
                    raise TypeError(
                        f"'{compare}' not supported between instances of '{type_other}' and '{type(val)}'")
        elif type_other in type_numbers[1:3]:
            for val in numbers[:3]:
                result.append(eval(f'type_other(val) {compare} other'))
        elif isinstance(other, complex) and compare in ('==', '!='):
            for val in numbers[:4]:
                result.append(eval(f'type_other(val) {compare} other'))
        elif isinstance(other, dict) and compare in ('==', '!='):
            result.append(eval(f'self.dictionary {compare} other'))
        else:
            for val in self._all_types:
                try:
                    if hasattr(val, '__iter__'):
                        result.append(eval(f'type_other(val) {compare} other'))
                    else:
                        result.append(eval(f'type_other([val]) {compare} other'))
                except (TypeError, ValueError):
                    result.append('Does not compare!')

        return tuple(result)

    def _arithmetic(self, other: Any, symbol: Literal = '+', layout_self: str = 'left', modulo: Numbers = None) -> Tuple[Any]:
        name_all_types: Tuple[str] = ('boolean', 'integer', 'float_num', 'complex_num', 'string', 'array', 'tuple_',
                                      'dictionary', 'set_', 'frozenset_')
        numbers: Tuple[Numbers] = (self.boolean, self.integer, self.float_num, self.complex_num)
        type_numbers: Tuple[Numbers] = tuple(map(type, numbers))
        binary_operators: Tuple[Literal] = ('<<', '>>', '&', '|', '^')
        result: List[Any] = []
        templates: CodeTemplate = ('for val in self._all_types{segment}:{before_expression}result.append({expression})'
                                   '{after_expression}', 'for name in name_all_types{segment}:{before_expression}'
                                                         'self.__dict__[name]{expression}{after_expression}')

        def define_layout(code_left_layout: CodeTemplate = '', code_right_layout: CodeTemplate = '',
                          code_equally: CodeTemplate = ''):
            allowed_vars: Dict[str, Any] = {'layout_self': layout_self, 'modulo': modulo, 'other': other, 'self': self,
                                            '__builtins__': {'pow': pow, 'hasattr': hasattr, 'print': print, 'str': str,
                                                             'divmod': divmod, 'complex': complex, 'int': int,
                                                             'ValueError': ValueError, 'float': float, 'dict': dict,
                                                             'isinstance': isinstance, 'type': type, 'bool': bool,
                                                             'set': set, 'frozenset': frozenset}, 'self': self,
                                            'result': result, 'hasattr': hasattr, 'code_left_layout': code_left_layout,
                                            'name_all_types': name_all_types, 'code_equally': code_equally,
                                            'code_right_layout': code_right_layout,  'type_numbers': type_numbers}
            if layout_self == 'left':
                exec(code_left_layout, allowed_vars)
            elif layout_self == 'right':
                exec(code_right_layout, allowed_vars)
            else:
                exec(code_equally, allowed_vars)

        if symbol in ('-', '&', '|', '^') and isinstance(other, (set, frozenset)):
            repeating_code: CodeTemplate = ('\n\tif hasattr(val, \'__iter__\'): result.append(', ')\n\telse:')
            same_parameters: Dict[str, CodeTemplate] = dict(segment='', after_expression='')
            define_layout(templates[0].format(before_expression=repeating_code[0] + f'type(other)(val) {symbol} other'
                                                                + repeating_code[1], **same_parameters,
                                              expression=f'type(other)([val]) {symbol} other'),
                          templates[0].format(before_expression=repeating_code[0] + f'other {symbol} type(other)(val)'
                                                                + repeating_code[1], **same_parameters,
                                              expression=f'other {symbol} type(other)([val])'),
                          templates[1].format(segment='[8:]', before_expression='', after_expression='',
                                              expression=f' = type(other)(self.__dict__[name]) {symbol} other'))
        elif symbol in binary_operators:
            same_parameters: Dict[str, CodeTemplate] = dict(segment='[:3]', before_expression='\n\t',
                                                            after_expression='')
            define_layout(templates[0].format(expression=f'int(val) {symbol} other', **same_parameters),
                          templates[0].format(segment='[:3]', before_expression='\n\ttry: ',
                                              expression=f'other {symbol} int(val)',
                                              after_expression='\n\texcept ValueError: result.append(f"{val} < 0")'),
                          templates[1].format(expression=f'=int(self.__dict__[name]){symbol}other', **same_parameters))
        elif symbol == '**':
            define_layout(templates[0].format(segment='[:4]', before_expression='\n\tif modulo is not None:\n\t\t'
                                                                                'if type(val) is not complex: ',
                                              expression='pow(int(val), other, modulo)',
                                              after_expression='\n\telse: result.append(pow(val, other, modulo))'),
                          templates[0].format(segment='[:4]', expression='pow(other, int(val), modulo)',
                                              after_expression='\n\telse: result.append(pow(other, val, modulo))',
                                              before_expression='\n\tif modulo is not None:\n\t\tif type(val) is not '
                                                                'complex: '),
                          templates[1].format(segment='[:4]', before_expression='\n\t', expression=f'{symbol}= other',
                                              after_expression=''))
        elif symbol in ('//', '%'):
            same_parameters: Dict[str, CodeTemplate] = dict(segment='[:3]', before_expression='\n\t',
                                                            after_expression='')
            define_layout(templates[0].format(expression=f'val {symbol} other', **same_parameters),
                          templates[0].format(expression=f'other {symbol} val', **same_parameters),
                          templates[1].format(expression=f' {symbol}= other', **same_parameters))
        elif symbol == 'divmod':
            same_parameters: Dict[str, CodeTemplate] = dict(before_expression='\n\t', after_expression='',
                                                            segment='[:3]')
            define_layout(templates[0].format(expression='divmod(val, other)', **same_parameters),
                          templates[0].format(expression='divmod(other, val)', **same_parameters))
        elif symbol in ('/', '-'):
            same_parameters: Dict[str, CodeTemplate] = dict(segment='[:4]', before_expression='\n\t',
                                                            after_expression='')
            define_layout(templates[0].format(expression=f'val {symbol} other', **same_parameters),
                          templates[0].format(expression=f'other {symbol} val', **same_parameters),
                          templates[1].format(expression=f' {symbol}= other', **same_parameters))
        elif symbol == '*':
            same_parameters: Dict[str, CodeTemplate] = dict(before_expression='\n\t', after_expression='')
            define_layout(templates[0].format(segment='[:4]' if isinstance(other, (complex, float)) else '[:7]',
                                              expression=f'val {symbol} other', **same_parameters),
                          templates[0].format(segment='[:4]' if type(other) in type_numbers else '[:2]',
                                              expression=f'other {symbol} val', **same_parameters),
                          templates[1].format(segment='[:4]' if isinstance(other, (complex, float)) else '[:7]',
                                              expression=f' = self.__dict__[name] {symbol} other', **same_parameters))
        elif symbol == '+':
            segment_ = '' if isinstance(other, (bool, str)) or hasattr(other, '__iter__') else '[:4]'
            repeating_code: CodeTemplate = '\n\tif isinstance(other, (bool, str)):result.append({expression_1})\n\t' \
                                           'elif isinstance(other, type_numbers):result.append({expression_2})\n\t' \
                                           'elif hasattr(val, "__iter__"):'
            define_layout(templates[0].format(segment=segment_, expression='type(other)(val) + other',
                                              before_expression=repeating_code.format(expression_1='type(other)(val)'
                                                                                                   '+ other',
                                                                                      expression_2='val + other'),
                                              after_expression='\n\telse:result.append(type(other)([val]) + other)'),
                          templates[0].format(segment=segment_, expression='other + type(other)(val)',
                                              before_expression=repeating_code.format(expression_1='other'
                                                                                                   '+ type(other)(val)',
                                                                                      expression_2='other + val'),
                                              after_expression='\n\telse:result.append(other + type(other)([val]))'),
                          templates[1].format(before_expression='\n\tif isinstance(other, type_numbers):'
                                                                'self.__dict__[name] = self.__dict__[name] + other\n\t'
                                                                'else:\n\t\tif name == "dictionary": continue\n\t\telif'
                                                                ' isinstance(self.__dict__[name], (set, frozenset)):'
                                                                '\n\t\t\tself.__dict__[name] = self.__dict__[name]'
                                                                ' | type(self.__dict__[name])(other)\n\t\t\t',
                                              expression='=self.__dict__[name] | type(self.__dict__[name])(other)'
                                                         '\n\t\t\t',
                                              after_expression='continue\n\t\tself.__dict__[name] = self.__dict__[name]'
                                                               ' + type(self.__dict__[name])(other)',
                                              segment='[:4]' if isinstance(other, type_numbers) else '[4:]'))

        return tuple(result)

    def __eq__(self, other: Any) -> Tuple[bool]:
        return self._comparison(other)

    def __ne__(self, other: Any) -> Tuple[bool]:
        return self._comparison(other, '!=')

    def __lt__(self, other: Any) -> Tuple[bool]:
        return self._comparison(other, '<')

    def __gt__(self, other: Any) -> Tuple[bool]:
        return self._comparison(other, '>')

    def __le__(self, other: Any) -> Tuple[bool]:
        return self._comparison(other, '<=')

    def __ge__(self, other: Any) -> Tuple[bool]:
        return self._comparison(other, '>=')

    # =====================================================================

    def __pos__(self) -> Tuple[Numbers]:
        return +self.boolean, +self.integer, +self.float_num, +self.complex_num

    def __neg__(self) -> Tuple[Numbers]:
        return -self.boolean, -self.integer, -self.float_num, -self.complex_num

    def __abs__(self) -> Tuple[int, float, complex]:
        return abs(self.integer), abs(self.float_num), abs(self.complex_num)

    def __round__(self, n: int = None) -> float:
        return round(self.float_num, n)

    def __floor__(self) -> float:
        return self.floor(self.float_num)

    def __ceil__(self) -> float:
        return self.ceil(self.float_num)

    def __trunc__(self) -> float:
        return self.trunc(self.float_num)

    # =====================================================================

    def __add__(self, other: BuiltInTypes) -> Tuple[BuiltInTypes]:
        if type(other) is set or type(other) is frozenset:
            return self._arithmetic(other, '|')
        return self._arithmetic(other)

    def __sub__(self, other: NumOrSet) -> Tuple[Numbers] or Tuple[set or frozenset]:
        return self._arithmetic(other, '-')

    def __mul__(self, other: Numbers) -> Tuple[Numbers] or Tuple[BuiltInTypes]:
        return self._arithmetic(other, '*')

    def __truediv__(self, other: Numbers) -> Tuple[Numbers]:
        return self._arithmetic(other, '/')

    def __floordiv__(self, other: bool or int or float) -> Tuple[bool, int, float]:
        return self._arithmetic(other, '//')

    def __mod__(self, other: bool or int or float) -> Tuple[bool, int, float]:
        return self._arithmetic(other, '%')

    def __divmod__(self, other: bool or int or float) -> Tuple[bool, int, float]:
        return self._arithmetic(other, 'divmod')

    def __pow__(self, power: Numbers, modulo: Numbers = None) -> Tuple[Numbers]:
        return self._arithmetic(power, '**', modulo=modulo)

    def __lshift__(self, other: int) -> Tuple[int]:
        return self._arithmetic(other, '<<')

    def __rshift__(self, other: int) -> Tuple[int]:
        return self._arithmetic(other, '>>')

    def __and__(self, other: NumWithoutComplexOrSet) -> Tuple[int] or Tuple[set or frozenset]:
        return self._arithmetic(other, '&')

    def __or__(self, other: NumWithoutComplexOrSet) -> Tuple[int] or Tuple[set or frozenset]:
        return self._arithmetic(other, '|')

    def __xor__(self, other: NumWithoutComplexOrSet) -> Tuple[int] or Tuple[set or frozenset]:
        return self._arithmetic(other, '^')

    # ---------------------------------------------------------------------

    def __radd__(self, other: BuiltInTypes) -> Tuple[BuiltInTypes]:
        if type(other) is set or type(other) is frozenset:
            return self._arithmetic(other, '|', 'right')
        return self._arithmetic(other, '+', 'right')

    def __rsub__(self, other: NumOrSet) -> Tuple[Numbers] or Tuple[set or frozenset]:
        return self._arithmetic(other, '-', 'right')

    def __rmul__(self, other: Any) -> Tuple[Any]:
        return self._arithmetic(other, '*', 'right')

    def __rtruediv__(self, other: Numbers) -> Tuple[Numbers]:
        return self._arithmetic(other, '/', 'right')

    def __rfloordiv__(self, other: bool or int or float) -> Tuple[bool, int, float]:
        return self._arithmetic(other, '//', 'right')

    def __rmod__(self, other: bool or int or float) -> Tuple[bool, int, float]:
        return self._arithmetic(other, '%', 'right')

    def __rdivmod__(self, other: bool or int or float) -> Tuple[bool, int, float]:
        return self._arithmetic(other, 'divmod', 'right')

    def __rpow__(self, power: Numbers, modulo: Numbers = None) -> Tuple[Numbers]:
        return self._arithmetic(power, '**', 'right', modulo)

    def __rlshift__(self, other: int) -> Tuple[int]:
        return self._arithmetic(other, '<<', 'right')

    def __rrshift__(self, other: int) -> Tuple[int]:
        return self._arithmetic(other, '>>', 'right')

    def __rand__(self, other: NumWithoutComplexOrSet) -> Tuple[int] or Tuple[set or frozenset]:
        return self._arithmetic(other, '&', 'right')

    def __ror__(self, other: NumWithoutComplexOrSet) -> Tuple[int] or Tuple[set or frozenset]:
        return self._arithmetic(other, '|', 'right')

    def __rxor__(self, other: NumWithoutComplexOrSet) -> Tuple[int] or Tuple[set or frozenset]:
        return self._arithmetic(other, '^', 'right')

    # ---------------------------------------------------------------------

    def __iadd__(self, other: NumOrSet) -> ClassInstance:
        if type(other) is set or type(other) is frozenset:
            self._arithmetic(other, '|', 'equally')
            return self
        self._arithmetic(other, '+', 'equally')
        return self

    def __isub__(self, other: NumOrSet) -> ClassInstance:
        self._arithmetic(other, '-', 'equally')
        return self

    def __imul__(self, other: Numbers) -> ClassInstance:
        self._arithmetic(other, '*', 'equally')
        return self

    def __itruediv__(self, other: Numbers) -> ClassInstance:
        self._arithmetic(other, '/', 'equally')
        return self

    def __ifloordiv__(self, other: bool or int or float) -> ClassInstance:
        self._arithmetic(other, '//', 'equally')
        return self

    def __imod__(self, other: bool or int or float) -> ClassInstance:
        self._arithmetic(other, '%', 'equally')
        return self

    def __ipow__(self, power: Numbers, modulo: Numbers = None) -> ClassInstance:
        self._arithmetic(power, '**', 'equally', modulo)
        return self

    def __ilshift__(self, other: int) -> ClassInstance:
        self._arithmetic(other, '<<', 'equally')
        return self

    def __irshift__(self, other: int) -> ClassInstance:
        self._arithmetic(other, '>>', 'equally')
        return self

    def __iand__(self, other: int or set or frozenset) -> ClassInstance:
        self._arithmetic(other, '&', 'equally')
        return self

    def __ior__(self, other: int or set or frozenset) -> ClassInstance:
        self._arithmetic(other, '|', 'equally')
        return self

    def __ixor__(self, other: int or set or frozenset) -> ClassInstance:
        self._arithmetic(other, '^', 'equally')
        return self

    # =====================================================================

    def _translate_in_type(self, type_conversion: type, *args) -> Any:
        """Trying to translate a string to the specified type. If it fails, translates what is specified in args."""
        try:
            return type_conversion(self.string)
        except (ValueError, TypeError):
            return type_conversion(*args)

    def __int__(self) -> int:
        """Translate float number in integer. if it can translate the string to integer then it will return it."""
        return self._translate_in_type(int, self.float_num)

    def __float__(self) -> float:
        """Translate integer number in float. if it can translate the string to float then it will return it."""
        return self._translate_in_type(float, self.integer)

    def __complex__(self) -> complex:
        """
        Translate integer and float number in complex. if it can translate the string to complex then it will return it.

        Real number will be integer, imaginary will be float.
        """
        return self._translate_in_type(complex, self.integer, self.float_num)

    # __oct__ and __hex__ do not working when define argument self(created object user) in
    # built-in function oct() and hex()
    def __oct__(self) -> IntString:
        return self._translate_in_type(oct, self.integer)

    def __hex__(self) -> IntString:
        return self._translate_in_type(hex, self.integer)

    def __index__(self) -> int:
        return self.integer

    def __str__(self) -> str:
        return f'<class {self.__class__.__name__} instance at {hex(id(self))}>'

    def __repr__(self) -> str:
        return str(self)

    def __format__(self, format_spec: AnyStr) -> AnyStr:
        return self.string

    def __hash__(self) -> int:
        """Returns a hash of a tuple in which all hashable types."""
        result = []
        for i in self._all_types:
            try:
                hash(i)
                result.append(i)
            except TypeError:
                pass
        return hash(tuple(result))

    def __bool__(self):
        return any(map(bool, self._all_types))

    def __dir__(self) -> Dict[str, Any]:
        return super().__dir__()

    def __sizeof__(self) -> int:
        return super().__sizeof__()

    def __getattr__(self, item: str) -> None:
        raise AttributeError(f'{str(self)} has not attribute {item}')

    def __len__(self) -> int:
        return len(self._all_types)

    def __getitem__(self, item: int) -> Any:
        return self._all_types[item]

    def __iter__(self) -> Iterator:
        self._index_value = 0
        return self

    def __next__(self):
        if self._index_value >= len(self._all_types):
            raise StopIteration
        value = self._all_types[self._index_value]
        self._index_value += 1
        return value

    def __reversed__(self) -> Tuple[Any]:
        return self._all_types[::-1]

    def __contains__(self, item: Any) -> bool:
        return item in self._all_types

    def __instancecheck__(self, instance: object) -> bool:
        return type(instance) is type(self)

    def __subclasscheck__(self, subclass: object) -> bool:
        return issubclass(subclass, self.__class__)

    def __call__(self, *args, **kwargs) -> Dict[str, Any]:
        """
        If the user has added the called object(s), all called objects are called and all parameters that are
        specified when the instance is called are passed. A dictionary is returned with the name of the called object
        and the value that it returns.
        """
        callable_obj: List[Callable[[Any], Any]] = []
        result_funcs: Dict[str, Any] = {}

        for obj in self.__dict__.values():
            if callable(obj):
                callable_obj.append(obj)
        if callable_obj:
            for call_obj in callable_obj:
                result_funcs[call_obj.__name__] = call_obj(*args, **kwargs)
        return result_funcs

    # Context manager
    def __enter__(self) -> Tuple[FileObj]:
        """Looks for an object that has the attribute "close", and returns a list of these objects."""
        file_obj: FileObj = []
        for obj in self.__dict__.values():
            if hasattr(obj, 'close'):
                file_obj.append(obj)
        return tuple(file_obj)

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Looks for an object that has the attribute "close", and call method "close"."""
        for obj in self.__dict__.values():
            if hasattr(obj, 'close'):
                obj.close()
    # End context manager

    def __copy__(self) -> ClassInstance:
        copy_obj = AllTypes()
        copy_obj.__dict__ = self.__dict__.copy()
        return copy_obj

    def __deepcopy__(self, memodict={}) -> ClassInstance:
        deepcopy_obj = AllTypes()
        deepcopy_obj.__dict__ = self.deepcopy(self.__dict__)
        return deepcopy_obj
