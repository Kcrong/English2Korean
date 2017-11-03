"""
Convert Javascript to Python with JS2PY

Special Thanks: https://github.com/e-/Hangul.js

"""

__all__ = ['hangul']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['_isJongJoinable', 'COMPLEX_CONSONANTS', '_makeHash', 'disassembleToString', 'hangul', '_isJung', 'assemble', 'COMPLETE_JONG', 'rangeSearch', '_isJong', 'JUNG_HASH', '_isJungJoinable', 'CHO_HASH', '_isCho', 'endsWithConsonant', '_isHangul', 'Searcher', '_isConsonant', '_makeComplexHash', 'CONSONANTS', 'COMPLETE_JUNG', 'CHO', 'CONSONANTS_HASH', 'COMPLEX_VOWELS_HASH', 'JONG', 'COMPLETE_CHO', 'COMPLEX_CONSONANTS_HASH', 'JONG_HASH', 'disassemble', 'JUNG', 'COMPLEX_VOWELS', 'search', 'HANGUL_OFFSET'])
@Js
def PyJsHoisted__makeHash_(array, this, arguments, var=var):
    var = Scope({'array':array, 'this':this, 'arguments':arguments}, var)
    var.registers(['array', 'length', 'i', 'hash'])
    var.put('length', var.get('array').get('length'))
    PyJs_Object_0_ = Js({'0':Js(0.0)})
    var.put('hash', PyJs_Object_0_)
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('length')):
        try:
            if var.get('array').get(var.get('i')):
                var.get('hash').put(var.get('array').get(var.get('i')).callprop('charCodeAt', Js(0.0)), var.get('i'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('hash')
PyJsHoisted__makeHash_.func_name = '_makeHash'
var.put('_makeHash', PyJsHoisted__makeHash_)
@Js
def PyJsHoisted__makeComplexHash_(array, this, arguments, var=var):
    var = Scope({'array':array, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'array', 'code1', 'hash', 'length', 'code2'])
    var.put('length', var.get('array').get('length'))
    PyJs_Object_1_ = Js({})
    var.put('hash', PyJs_Object_1_)
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('length')):
        try:
            var.put('code1', var.get('array').get(var.get('i')).get('0').callprop('charCodeAt', Js(0.0)))
            var.put('code2', var.get('array').get(var.get('i')).get('1').callprop('charCodeAt', Js(0.0)))
            if PyJsStrictEq(var.get('hash').get(var.get('code1')).typeof(),Js('undefined')):
                PyJs_Object_2_ = Js({})
                var.get('hash').put(var.get('code1'), PyJs_Object_2_)
            var.get('hash').get(var.get('code1')).put(var.get('code2'), var.get('array').get(var.get('i')).get('2').callprop('charCodeAt', Js(0.0)))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('hash')
PyJsHoisted__makeComplexHash_.func_name = '_makeComplexHash'
var.put('_makeComplexHash', PyJsHoisted__makeComplexHash_)
@Js
def PyJsHoisted__isConsonant_(c, this, arguments, var=var):
    var = Scope({'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['c'])
    return PyJsStrictNeq(var.get('CONSONANTS_HASH').get(var.get('c')).typeof(),Js('undefined'))
PyJsHoisted__isConsonant_.func_name = '_isConsonant'
var.put('_isConsonant', PyJsHoisted__isConsonant_)
@Js
def PyJsHoisted__isCho_(c, this, arguments, var=var):
    var = Scope({'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['c'])
    return PyJsStrictNeq(var.get('CHO_HASH').get(var.get('c')).typeof(),Js('undefined'))
PyJsHoisted__isCho_.func_name = '_isCho'
var.put('_isCho', PyJsHoisted__isCho_)
@Js
def PyJsHoisted__isJung_(c, this, arguments, var=var):
    var = Scope({'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['c'])
    return PyJsStrictNeq(var.get('JUNG_HASH').get(var.get('c')).typeof(),Js('undefined'))
PyJsHoisted__isJung_.func_name = '_isJung'
var.put('_isJung', PyJsHoisted__isJung_)
@Js
def PyJsHoisted__isJong_(c, this, arguments, var=var):
    var = Scope({'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['c'])
    return PyJsStrictNeq(var.get('JONG_HASH').get(var.get('c')).typeof(),Js('undefined'))
PyJsHoisted__isJong_.func_name = '_isJong'
var.put('_isJong', PyJsHoisted__isJong_)
@Js
def PyJsHoisted__isHangul_(c, this, arguments, var=var):
    var = Scope({'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['c'])
    return ((Js(44032)<=var.get('c')) and (var.get('c')<=Js(55203)))
PyJsHoisted__isHangul_.func_name = '_isHangul'
var.put('_isHangul', PyJsHoisted__isHangul_)
@Js
def PyJsHoisted__isJungJoinable_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'b'])
    return (var.get('COMPLEX_VOWELS_HASH').get(var.get('a')).get(var.get('b')) if (var.get('COMPLEX_VOWELS_HASH').get(var.get('a')) and var.get('COMPLEX_VOWELS_HASH').get(var.get('a')).get(var.get('b'))) else Js(False))
PyJsHoisted__isJungJoinable_.func_name = '_isJungJoinable'
var.put('_isJungJoinable', PyJsHoisted__isJungJoinable_)
@Js
def PyJsHoisted__isJongJoinable_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'b'])
    return (var.get('COMPLEX_CONSONANTS_HASH').get(var.get('a')).get(var.get('b')) if (var.get('COMPLEX_CONSONANTS_HASH').get(var.get('a')) and var.get('COMPLEX_CONSONANTS_HASH').get(var.get('a')).get(var.get('b'))) else Js(False))
PyJsHoisted__isJongJoinable_.func_name = '_isJongJoinable'
var.put('_isJongJoinable', PyJsHoisted__isJongJoinable_)
@Js
def PyJsHoisted_Searcher_(string, this, arguments, var=var):
    var = Scope({'string':string, 'this':this, 'arguments':arguments}, var)
    var.registers(['string'])
    var.get(u"this").put('string', var.get('string'))
    var.get(u"this").put('disassembled', var.get('disassemble')(var.get('string')).callprop('join', Js('')))
PyJsHoisted_Searcher_.func_name = 'Searcher'
var.put('Searcher', PyJsHoisted_Searcher_)
var.put('CHO', Js([Js('ㄱ'), Js('ㄲ'), Js('ㄴ'), Js('ㄷ'), Js('ㄸ'), Js('ㄹ'), Js('ㅁ'), Js('ㅂ'), Js('ㅃ'), Js('ㅅ'), Js('ㅆ'), Js('ㅇ'), Js('ㅈ'), Js('ㅉ'), Js('ㅊ'), Js('ㅋ'), Js('ㅌ'), Js('ㅍ'), Js('ㅎ')]))
var.put('JUNG', Js([Js('ㅏ'), Js('ㅐ'), Js('ㅑ'), Js('ㅒ'), Js('ㅓ'), Js('ㅔ'), Js('ㅕ'), Js('ㅖ'), Js('ㅗ'), Js([Js('ㅗ'), Js('ㅏ')]), Js([Js('ㅗ'), Js('ㅐ')]), Js([Js('ㅗ'), Js('ㅣ')]), Js('ㅛ'), Js('ㅜ'), Js([Js('ㅜ'), Js('ㅓ')]), Js([Js('ㅜ'), Js('ㅔ')]), Js([Js('ㅜ'), Js('ㅣ')]), Js('ㅠ'), Js('ㅡ'), Js([Js('ㅡ'), Js('ㅣ')]), Js('ㅣ')]))
var.put('JONG', Js([Js(''), Js('ㄱ'), Js('ㄲ'), Js([Js('ㄱ'), Js('ㅅ')]), Js('ㄴ'), Js([Js('ㄴ'), Js('ㅈ')]), Js([Js('ㄴ'), Js('ㅎ')]), Js('ㄷ'), Js('ㄹ'), Js([Js('ㄹ'), Js('ㄱ')]), Js([Js('ㄹ'), Js('ㅁ')]), Js([Js('ㄹ'), Js('ㅂ')]), Js([Js('ㄹ'), Js('ㅅ')]), Js([Js('ㄹ'), Js('ㅌ')]), Js([Js('ㄹ'), Js('ㅍ')]), Js([Js('ㄹ'), Js('ㅎ')]), Js('ㅁ'), Js('ㅂ'), Js([Js('ㅂ'), Js('ㅅ')]), Js('ㅅ'), Js('ㅆ'), Js('ㅇ'), Js('ㅈ'), Js('ㅊ'), Js('ㅋ'), Js('ㅌ'), Js('ㅍ'), Js('ㅎ')]))
var.put('HANGUL_OFFSET', Js(44032))
var.put('CONSONANTS', Js([Js('ㄱ'), Js('ㄲ'), Js('ㄳ'), Js('ㄴ'), Js('ㄵ'), Js('ㄶ'), Js('ㄷ'), Js('ㄸ'), Js('ㄹ'), Js('ㄺ'), Js('ㄻ'), Js('ㄼ'), Js('ㄽ'), Js('ㄾ'), Js('ㄿ'), Js('ㅀ'), Js('ㅁ'), Js('ㅂ'), Js('ㅃ'), Js('ㅄ'), Js('ㅅ'), Js('ㅆ'), Js('ㅇ'), Js('ㅈ'), Js('ㅉ'), Js('ㅊ'), Js('ㅋ'), Js('ㅌ'), Js('ㅍ'), Js('ㅎ')]))
var.put('COMPLETE_CHO', Js([Js('ㄱ'), Js('ㄲ'), Js('ㄴ'), Js('ㄷ'), Js('ㄸ'), Js('ㄹ'), Js('ㅁ'), Js('ㅂ'), Js('ㅃ'), Js('ㅅ'), Js('ㅆ'), Js('ㅇ'), Js('ㅈ'), Js('ㅉ'), Js('ㅊ'), Js('ㅋ'), Js('ㅌ'), Js('ㅍ'), Js('ㅎ')]))
var.put('COMPLETE_JUNG', Js([Js('ㅏ'), Js('ㅐ'), Js('ㅑ'), Js('ㅒ'), Js('ㅓ'), Js('ㅔ'), Js('ㅕ'), Js('ㅖ'), Js('ㅗ'), Js('ㅘ'), Js('ㅙ'), Js('ㅚ'), Js('ㅛ'), Js('ㅜ'), Js('ㅝ'), Js('ㅞ'), Js('ㅟ'), Js('ㅠ'), Js('ㅡ'), Js('ㅢ'), Js('ㅣ')]))
var.put('COMPLETE_JONG', Js([Js(''), Js('ㄱ'), Js('ㄲ'), Js('ㄳ'), Js('ㄴ'), Js('ㄵ'), Js('ㄶ'), Js('ㄷ'), Js('ㄹ'), Js('ㄺ'), Js('ㄻ'), Js('ㄼ'), Js('ㄽ'), Js('ㄾ'), Js('ㄿ'), Js('ㅀ'), Js('ㅁ'), Js('ㅂ'), Js('ㅄ'), Js('ㅅ'), Js('ㅆ'), Js('ㅇ'), Js('ㅈ'), Js('ㅊ'), Js('ㅋ'), Js('ㅌ'), Js('ㅍ'), Js('ㅎ')]))
var.put('COMPLEX_CONSONANTS', Js([Js([Js('ㄱ'), Js('ㅅ'), Js('ㄳ')]), Js([Js('ㄴ'), Js('ㅈ'), Js('ㄵ')]), Js([Js('ㄴ'), Js('ㅎ'), Js('ㄶ')]), Js([Js('ㄹ'), Js('ㄱ'), Js('ㄺ')]), Js([Js('ㄹ'), Js('ㅁ'), Js('ㄻ')]), Js([Js('ㄹ'), Js('ㅂ'), Js('ㄼ')]), Js([Js('ㄹ'), Js('ㅅ'), Js('ㄽ')]), Js([Js('ㄹ'), Js('ㅌ'), Js('ㄾ')]), Js([Js('ㄹ'), Js('ㅍ'), Js('ㄿ')]), Js([Js('ㄹ'), Js('ㅎ'), Js('ㅀ')]), Js([Js('ㅂ'), Js('ㅅ'), Js('ㅄ')])]))
var.put('COMPLEX_VOWELS', Js([Js([Js('ㅗ'), Js('ㅏ'), Js('ㅘ')]), Js([Js('ㅗ'), Js('ㅐ'), Js('ㅙ')]), Js([Js('ㅗ'), Js('ㅣ'), Js('ㅚ')]), Js([Js('ㅜ'), Js('ㅓ'), Js('ㅝ')]), Js([Js('ㅜ'), Js('ㅔ'), Js('ㅞ')]), Js([Js('ㅜ'), Js('ㅣ'), Js('ㅟ')]), Js([Js('ㅡ'), Js('ㅣ'), Js('ㅢ')])]))
pass
var.put('CONSONANTS_HASH', var.get('_makeHash')(var.get('CONSONANTS')))
var.put('CHO_HASH', var.get('_makeHash')(var.get('COMPLETE_CHO')))
var.put('JUNG_HASH', var.get('_makeHash')(var.get('COMPLETE_JUNG')))
var.put('JONG_HASH', var.get('_makeHash')(var.get('COMPLETE_JONG')))
pass
var.put('COMPLEX_CONSONANTS_HASH', var.get('_makeComplexHash')(var.get('COMPLEX_CONSONANTS')))
var.put('COMPLEX_VOWELS_HASH', var.get('_makeComplexHash')(var.get('COMPLEX_VOWELS')))
pass
pass
pass
pass
pass
pass
pass
@Js
def PyJs_anonymous_3_(string, grouped, this, arguments, var=var):
    var = Scope({'string':string, 'grouped':grouped, 'this':this, 'arguments':arguments}, var)
    var.registers(['code', 'jung', 'cho', 'string', 'result', 'i', 'temp', 'grouped', 'length', 'jong', 'r'])
    if PyJsStrictEq(var.get('string'),var.get(u"null")):
        PyJsTempException = JsToPyException(var.get('Error').create(Js('Arguments cannot be null')))
        raise PyJsTempException
    if PyJsStrictEq(var.get('string',throw=False).typeof(),Js('object')):
        var.put('string', var.get('string').callprop('join', Js('')))
    var.put('result', Js([]))
    var.put('length', var.get('string').get('length'))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('length')):
        try:
            var.put('temp', Js([]))
            var.put('code', var.get('string').callprop('charCodeAt', var.get('i')))
            if var.get('_isHangul')(var.get('code')):
                var.put('code', var.get('HANGUL_OFFSET'), '-')
                var.put('jong', (var.get('code')%Js(28.0)))
                var.put('jung', (((var.get('code')-var.get('jong'))/Js(28.0))%Js(21.0)))
                var.put('cho', var.get('parseInt')((((var.get('code')-var.get('jong'))/Js(28.0))/Js(21.0))))
                var.get('temp').callprop('push', var.get('CHO').get(var.get('cho')))
                if PyJsStrictEq(var.get('JUNG').get(var.get('jung')).typeof(),Js('object')):
                    var.put('temp', var.get('temp').callprop('concat', var.get('JUNG').get(var.get('jung'))))
                else:
                    var.get('temp').callprop('push', var.get('JUNG').get(var.get('jung')))
                if (var.get('jong')>Js(0.0)):
                    if PyJsStrictEq(var.get('JONG').get(var.get('jong')).typeof(),Js('object')):
                        var.put('temp', var.get('temp').callprop('concat', var.get('JONG').get(var.get('jong'))))
                    else:
                        var.get('temp').callprop('push', var.get('JONG').get(var.get('jong')))
            else:
                if var.get('_isConsonant')(var.get('code')):
                    if var.get('_isCho')(var.get('code')):
                        var.put('r', var.get('CHO').get(var.get('CHO_HASH').get(var.get('code'))))
                    else:
                        var.put('r', var.get('JONG').get(var.get('JONG_HASH').get(var.get('code'))))
                    if PyJsStrictEq(var.get('r',throw=False).typeof(),Js('string')):
                        var.get('temp').callprop('push', var.get('r'))
                    else:
                        var.put('temp', var.get('temp').callprop('concat', var.get('r')))
                else:
                    if var.get('_isJung')(var.get('code')):
                        var.put('r', var.get('JUNG').get(var.get('JUNG_HASH').get(var.get('code'))))
                        if PyJsStrictEq(var.get('r',throw=False).typeof(),Js('string')):
                            var.get('temp').callprop('push', var.get('r'))
                        else:
                            var.put('temp', var.get('temp').callprop('concat', var.get('r')))
                    else:
                        var.get('temp').callprop('push', var.get('string').callprop('charAt', var.get('i')))
            if var.get('grouped'):
                var.get('result').callprop('push', var.get('temp'))
            else:
                var.put('result', var.get('result').callprop('concat', var.get('temp')))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('result')
PyJs_anonymous_3_._set_name('anonymous')
var.put('disassemble', PyJs_anonymous_3_)
@Js
def PyJs_anonymous_4_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['str'])
    if PyJsStrictNeq(var.get('str',throw=False).typeof(),Js('string')):
        return Js('')
    var.put('str', var.get('disassemble')(var.get('str')))
    return var.get('str').callprop('join', Js(''))
PyJs_anonymous_4_._set_name('anonymous')
var.put('disassembleToString', PyJs_anonymous_4_)
@Js
def PyJs_anonymous_5_(array, this, arguments, var=var):
    var = Scope({'array':array, 'this':this, 'arguments':arguments}, var)
    var.registers(['previous_code', 'complete_index', 'result', 'i', 'stage', 'array', '_makeHangul', 'length', 'code'])
    @Js
    def PyJsHoisted__makeHangul_(index, this, arguments, var=var):
        var = Scope({'index':index, 'this':this, 'arguments':arguments}, var)
        var.registers(['hangul', 'cho', 'jong1', 'index', 'jung2', 'jung1', 'jong2', 'step', 'code'])
        var.put('jong1', Js(0.0))
        var.put('hangul', Js(''))
        if ((var.get('complete_index')+Js(1.0))>var.get('index')):
            return var.get('undefined')
        #for JS loop
        var.put('step', Js(1.0))
        while 1:
            try:
                if PyJsStrictEq(var.get('step'),Js(1.0)):
                    var.put('cho', var.get('array').get((var.get('complete_index')+var.get('step'))).callprop('charCodeAt', Js(0.0)))
                    if var.get('_isJung')(var.get('cho')):
                        if ((((var.get('complete_index')+var.get('step'))+Js(1.0))<=var.get('index')) and var.get('_isJung')(var.put('jung1', var.get('array').get(((var.get('complete_index')+var.get('step'))+Js(1.0))).callprop('charCodeAt', Js(0.0))))):
                            var.get('result').callprop('push', var.get('String').callprop('fromCharCode', var.get('_isJungJoinable')(var.get('cho'), var.get('jung1'))))
                            var.put('complete_index', var.get('index'))
                            return var.get('undefined')
                        else:
                            var.get('result').callprop('push', var.get('array').get((var.get('complete_index')+var.get('step'))))
                            var.put('complete_index', var.get('index'))
                            return var.get('undefined')
                    else:
                        if var.get('_isCho')(var.get('cho')).neg():
                            var.get('result').callprop('push', var.get('array').get((var.get('complete_index')+var.get('step'))))
                            var.put('complete_index', var.get('index'))
                            return var.get('undefined')
                    var.put('hangul', var.get('array').get((var.get('complete_index')+var.get('step'))))
                else:
                    if PyJsStrictEq(var.get('step'),Js(2.0)):
                        var.put('jung1', var.get('array').get((var.get('complete_index')+var.get('step'))).callprop('charCodeAt', Js(0.0)))
                        if var.get('_isCho')(var.get('jung1')):
                            var.put('cho', var.get('_isJongJoinable')(var.get('cho'), var.get('jung1')))
                            var.put('hangul', var.get('String').callprop('fromCharCode', var.get('cho')))
                            var.get('result').callprop('push', var.get('hangul'))
                            var.put('complete_index', var.get('index'))
                            return var.get('undefined')
                        else:
                            var.put('hangul', var.get('String').callprop('fromCharCode', ((((var.get('CHO_HASH').get(var.get('cho'))*Js(21.0))+var.get('JUNG_HASH').get(var.get('jung1')))*Js(28.0))+var.get('HANGUL_OFFSET'))))
                    else:
                        if PyJsStrictEq(var.get('step'),Js(3.0)):
                            var.put('jung2', var.get('array').get((var.get('complete_index')+var.get('step'))).callprop('charCodeAt', Js(0.0)))
                            if var.get('_isJungJoinable')(var.get('jung1'), var.get('jung2')):
                                var.put('jung1', var.get('_isJungJoinable')(var.get('jung1'), var.get('jung2')))
                            else:
                                var.put('jong1', var.get('jung2'))
                            var.put('hangul', var.get('String').callprop('fromCharCode', (((((var.get('CHO_HASH').get(var.get('cho'))*Js(21.0))+var.get('JUNG_HASH').get(var.get('jung1')))*Js(28.0))+var.get('JONG_HASH').get(var.get('jong1')))+var.get('HANGUL_OFFSET'))))
                        else:
                            if PyJsStrictEq(var.get('step'),Js(4.0)):
                                var.put('jong2', var.get('array').get((var.get('complete_index')+var.get('step'))).callprop('charCodeAt', Js(0.0)))
                                if var.get('_isJongJoinable')(var.get('jong1'), var.get('jong2')):
                                    var.put('jong1', var.get('_isJongJoinable')(var.get('jong1'), var.get('jong2')))
                                else:
                                    var.put('jong1', var.get('jong2'))
                                var.put('hangul', var.get('String').callprop('fromCharCode', (((((var.get('CHO_HASH').get(var.get('cho'))*Js(21.0))+var.get('JUNG_HASH').get(var.get('jung1')))*Js(28.0))+var.get('JONG_HASH').get(var.get('jong1')))+var.get('HANGUL_OFFSET'))))
                            else:
                                if PyJsStrictEq(var.get('step'),Js(5.0)):
                                    var.put('jong2', var.get('array').get((var.get('complete_index')+var.get('step'))).callprop('charCodeAt', Js(0.0)))
                                    var.put('jong1', var.get('_isJongJoinable')(var.get('jong1'), var.get('jong2')))
                                    var.put('hangul', var.get('String').callprop('fromCharCode', (((((var.get('CHO_HASH').get(var.get('cho'))*Js(21.0))+var.get('JUNG_HASH').get(var.get('jung1')))*Js(28.0))+var.get('JONG_HASH').get(var.get('jong1')))+var.get('HANGUL_OFFSET'))))
                if ((var.get('complete_index')+var.get('step'))>=var.get('index')):
                    var.get('result').callprop('push', var.get('hangul'))
                    var.put('complete_index', var.get('index'))
                    return var.get('undefined')
            finally:
                    (var.put('step',Js(var.get('step').to_number())+Js(1))-Js(1))
    PyJsHoisted__makeHangul_.func_name = '_makeHangul'
    var.put('_makeHangul', PyJsHoisted__makeHangul_)
    if PyJsStrictEq(var.get('array',throw=False).typeof(),Js('string')):
        var.put('array', var.get('disassemble')(var.get('array')))
    var.put('result', Js([]))
    var.put('length', var.get('array').get('length'))
    var.put('stage', Js(0.0))
    var.put('complete_index', (-Js(1.0)))
    pass
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('length')):
        try:
            var.put('code', var.get('array').get(var.get('i')).callprop('charCodeAt', Js(0.0)))
            if ((var.get('_isCho')(var.get('code')).neg() and var.get('_isJung')(var.get('code')).neg()) and var.get('_isJong')(var.get('code')).neg()):
                var.get('_makeHangul')((var.get('i')-Js(1.0)))
                var.get('_makeHangul')(var.get('i'))
                var.put('stage', Js(0.0))
                continue
            if PyJsStrictEq(var.get('stage'),Js(0.0)):
                if var.get('_isCho')(var.get('code')):
                    var.put('stage', Js(1.0))
                else:
                    if var.get('_isJung')(var.get('code')):
                        var.put('stage', Js(4.0))
            else:
                if (var.get('stage')==Js(1.0)):
                    if var.get('_isJung')(var.get('code')):
                        var.put('stage', Js(2.0))
                    else:
                        if var.get('_isJongJoinable')(var.get('previous_code'), var.get('code')):
                            var.put('stage', Js(5.0))
                        else:
                            var.get('_makeHangul')((var.get('i')-Js(1.0)))
                else:
                    if (var.get('stage')==Js(2.0)):
                        if var.get('_isJong')(var.get('code')):
                            var.put('stage', Js(3.0))
                        else:
                            if var.get('_isJung')(var.get('code')):
                                if var.get('_isJungJoinable')(var.get('previous_code'), var.get('code')):
                                    pass
                                else:
                                    var.get('_makeHangul')((var.get('i')-Js(1.0)))
                                    var.put('stage', Js(4.0))
                            else:
                                var.get('_makeHangul')((var.get('i')-Js(1.0)))
                                var.put('stage', Js(1.0))
                    else:
                        if (var.get('stage')==Js(3.0)):
                            if var.get('_isJong')(var.get('code')):
                                if var.get('_isJongJoinable')(var.get('previous_code'), var.get('code')):
                                    pass
                                else:
                                    var.get('_makeHangul')((var.get('i')-Js(1.0)))
                                    var.put('stage', Js(1.0))
                            else:
                                if var.get('_isCho')(var.get('code')):
                                    var.get('_makeHangul')((var.get('i')-Js(1.0)))
                                    var.put('stage', Js(1.0))
                                else:
                                    if var.get('_isJung')(var.get('code')):
                                        var.get('_makeHangul')((var.get('i')-Js(2.0)))
                                        var.put('stage', Js(2.0))
                        else:
                            if (var.get('stage')==Js(4.0)):
                                if var.get('_isJung')(var.get('code')):
                                    if var.get('_isJungJoinable')(var.get('previous_code'), var.get('code')):
                                        var.get('_makeHangul')(var.get('i'))
                                        var.put('stage', Js(0.0))
                                    else:
                                        var.get('_makeHangul')((var.get('i')-Js(1.0)))
                                else:
                                    var.get('_makeHangul')((var.get('i')-Js(1.0)))
                                    var.put('stage', Js(1.0))
                            else:
                                if (var.get('stage')==Js(5.0)):
                                    if var.get('_isJung')(var.get('code')):
                                        var.get('_makeHangul')((var.get('i')-Js(2.0)))
                                        var.put('stage', Js(2.0))
                                    else:
                                        var.get('_makeHangul')((var.get('i')-Js(1.0)))
                                        var.put('stage', Js(1.0))
            var.put('previous_code', var.get('code'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.get('_makeHangul')((var.get('i')-Js(1.0)))
    return var.get('result').callprop('join', Js(''))
PyJs_anonymous_5_._set_name('anonymous')
var.put('assemble', PyJs_anonymous_5_)
@Js
def PyJs_anonymous_6_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'a', 'bd', 'ad'])
    var.put('ad', var.get('disassemble')(var.get('a')).callprop('join', Js('')))
    var.put('bd', var.get('disassemble')(var.get('b')).callprop('join', Js('')))
    return var.get('ad').callprop('indexOf', var.get('bd'))
PyJs_anonymous_6_._set_name('anonymous')
var.put('search', PyJs_anonymous_6_)
@Js
def PyJs_anonymous_7_(haystack, needle, this, arguments, var=var):
    var = Scope({'haystack':haystack, 'needle':needle, 'this':this, 'arguments':arguments}, var)
    var.registers(['haystack', 're', 'nex', 'result', 'findStart', 'indices', 'hex', 'findEnd', 'grouped', 'needle'])
    @Js
    def PyJsHoisted_findStart_(index, this, arguments, var=var):
        var = Scope({'index':index, 'this':this, 'arguments':arguments}, var)
        var.registers(['length', 'i', 'index'])
        #for JS loop
        var.put('i', Js(0.0))
        var.put('length', Js(0.0))
        while (var.get('i')<var.get('grouped').get('length')):
            try:
                var.put('length', var.get('grouped').get(var.get('i')).get('length'), '+')
                if (var.get('index')<var.get('length')):
                    return var.get('i')
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
    PyJsHoisted_findStart_.func_name = 'findStart'
    var.put('findStart', PyJsHoisted_findStart_)
    @Js
    def PyJsHoisted_findEnd_(index, this, arguments, var=var):
        var = Scope({'index':index, 'this':this, 'arguments':arguments}, var)
        var.registers(['length', 'i', 'index'])
        #for JS loop
        var.put('i', Js(0.0))
        var.put('length', Js(0.0))
        while (var.get('i')<var.get('grouped').get('length')):
            try:
                var.put('length', var.get('grouped').get(var.get('i')).get('length'), '+')
                if ((var.get('index')+var.get('nex').get('length'))<=var.get('length')):
                    return var.get('i')
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
    PyJsHoisted_findEnd_.func_name = 'findEnd'
    var.put('findEnd', PyJsHoisted_findEnd_)
    var.put('hex', var.get('disassemble')(var.get('haystack')).callprop('join', Js('')))
    var.put('nex', var.get('disassemble')(var.get('needle')).callprop('join', Js('')))
    var.put('grouped', var.get('disassemble')(var.get('haystack'), Js(True)))
    var.put('re', var.get('RegExp').create(var.get('nex'), Js('gi')))
    var.put('indices', Js([]))
    if var.get('needle').get('length').neg():
        return Js([])
    while var.put('result', var.get('re').callprop('exec', var.get('hex'))):
        var.get('indices').callprop('push', var.get('result').get('index'))
    pass
    pass
    @Js
    def PyJs_anonymous_8_(i, this, arguments, var=var):
        var = Scope({'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['i'])
        return Js([var.get('findStart')(var.get('i')), var.get('findEnd')(var.get('i'))])
    PyJs_anonymous_8_._set_name('anonymous')
    return var.get('indices').callprop('map', PyJs_anonymous_8_)
PyJs_anonymous_7_._set_name('anonymous')
var.put('rangeSearch', PyJs_anonymous_7_)
pass
@Js
def PyJs_anonymous_9_(string, this, arguments, var=var):
    var = Scope({'string':string, 'this':this, 'arguments':arguments}, var)
    var.registers(['string'])
    return var.get('disassemble')(var.get('string')).callprop('join', Js('')).callprop('indexOf', var.get(u"this").get('disassembled'))
PyJs_anonymous_9_._set_name('anonymous')
var.get('Searcher').get('prototype').put('search', PyJs_anonymous_9_)
@Js
def PyJs_anonymous_10_(string, this, arguments, var=var):
    var = Scope({'string':string, 'this':this, 'arguments':arguments}, var)
    var.registers(['string', 'jong', 'code'])
    if PyJsStrictEq(var.get('string',throw=False).typeof(),Js('object')):
        var.put('string', var.get('string').callprop('join', Js('')))
    var.put('code', var.get('string').callprop('charCodeAt', (var.get('string').get('length')-Js(1.0))))
    if var.get('_isHangul')(var.get('code')):
        var.put('code', var.get('HANGUL_OFFSET'), '-')
        var.put('jong', (var.get('code')%Js(28.0)))
        if (var.get('jong')>Js(0.0)):
            return Js(True)
    else:
        if var.get('_isConsonant')(var.get('code')):
            return Js(True)
    return Js(False)
PyJs_anonymous_10_._set_name('anonymous')
var.put('endsWithConsonant', PyJs_anonymous_10_)
@Js
def PyJs_anonymous_12_(c, this, arguments, var=var):
    var = Scope({'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['c'])
    if PyJsStrictEq(var.get('c',throw=False).typeof(),Js('string')):
        var.put('c', var.get('c').callprop('charCodeAt', Js(0.0)))
    return var.get('_isHangul')(var.get('c'))
PyJs_anonymous_12_._set_name('anonymous')
@Js
def PyJs_anonymous_13_(c, this, arguments, var=var):
    var = Scope({'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['c'])
    if PyJsStrictEq(var.get('c',throw=False).typeof(),Js('string')):
        var.put('c', var.get('c').callprop('charCodeAt', Js(0.0)))
    return var.get('_isHangul')(var.get('c'))
PyJs_anonymous_13_._set_name('anonymous')
@Js
def PyJs_anonymous_14_(c, this, arguments, var=var):
    var = Scope({'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['c'])
    if PyJsStrictEq(var.get('c',throw=False).typeof(),Js('string')):
        var.put('c', var.get('c').callprop('charCodeAt', Js(0.0)))
    return var.get('_isConsonant')(var.get('c'))
PyJs_anonymous_14_._set_name('anonymous')
@Js
def PyJs_anonymous_15_(c, this, arguments, var=var):
    var = Scope({'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['c'])
    if PyJsStrictEq(var.get('c',throw=False).typeof(),Js('string')):
        var.put('c', var.get('c').callprop('charCodeAt', Js(0.0)))
    return var.get('_isJung')(var.get('c'))
PyJs_anonymous_15_._set_name('anonymous')
@Js
def PyJs_anonymous_16_(c, this, arguments, var=var):
    var = Scope({'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['c'])
    if PyJsStrictEq(var.get('c',throw=False).typeof(),Js('string')):
        var.put('c', var.get('c').callprop('charCodeAt', Js(0.0)))
    return var.get('_isCho')(var.get('c'))
PyJs_anonymous_16_._set_name('anonymous')
@Js
def PyJs_anonymous_17_(c, this, arguments, var=var):
    var = Scope({'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['c'])
    if PyJsStrictEq(var.get('c',throw=False).typeof(),Js('string')):
        var.put('c', var.get('c').callprop('charCodeAt', Js(0.0)))
    return var.get('_isJong')(var.get('c'))
PyJs_anonymous_17_._set_name('anonymous')
@Js
def PyJs_anonymous_18_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'str'])
    if PyJsStrictNeq(var.get('str',throw=False).typeof(),Js('string')):
        return Js(False)
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('str').get('length')):
        try:
            if var.get('_isHangul')(var.get('str').callprop('charCodeAt', var.get('i'))).neg():
                return Js(False)
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return Js(True)
PyJs_anonymous_18_._set_name('anonymous')
@Js
def PyJs_anonymous_19_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'str'])
    if PyJsStrictNeq(var.get('str',throw=False).typeof(),Js('string')):
        return Js(False)
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('str').get('length')):
        try:
            if var.get('_isHangul')(var.get('str').callprop('charCodeAt', var.get('i'))).neg():
                return Js(False)
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return Js(True)
PyJs_anonymous_19_._set_name('anonymous')
@Js
def PyJs_anonymous_20_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'str'])
    if PyJsStrictNeq(var.get('str',throw=False).typeof(),Js('string')):
        return Js(False)
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('str').get('length')):
        try:
            if var.get('_isConsonant')(var.get('str').callprop('charCodeAt', var.get('i'))).neg():
                return Js(False)
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return Js(True)
PyJs_anonymous_20_._set_name('anonymous')
@Js
def PyJs_anonymous_21_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'str'])
    if PyJsStrictNeq(var.get('str',throw=False).typeof(),Js('string')):
        return Js(False)
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('str').get('length')):
        try:
            if var.get('_isJung')(var.get('str').callprop('charCodeAt', var.get('i'))).neg():
                return Js(False)
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return Js(True)
PyJs_anonymous_21_._set_name('anonymous')
@Js
def PyJs_anonymous_22_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'str'])
    if PyJsStrictNeq(var.get('str',throw=False).typeof(),Js('string')):
        return Js(False)
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('str').get('length')):
        try:
            if var.get('_isCho')(var.get('str').callprop('charCodeAt', var.get('i'))).neg():
                return Js(False)
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return Js(True)
PyJs_anonymous_22_._set_name('anonymous')
@Js
def PyJs_anonymous_23_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'str'])
    if PyJsStrictNeq(var.get('str',throw=False).typeof(),Js('string')):
        return Js(False)
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('str').get('length')):
        try:
            if var.get('_isJong')(var.get('str').callprop('charCodeAt', var.get('i'))).neg():
                return Js(False)
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return Js(True)
PyJs_anonymous_23_._set_name('anonymous')
PyJs_Object_11_ = Js({'disassemble':var.get('disassemble'),'d':var.get('disassemble'),'disassembleToString':var.get('disassembleToString'),'ds':var.get('disassembleToString'),'assemble':var.get('assemble'),'a':var.get('assemble'),'search':var.get('search'),'rangeSearch':var.get('rangeSearch'),'Searcher':var.get('Searcher'),'endsWithConsonant':var.get('endsWithConsonant'),'isHangul':PyJs_anonymous_12_,'isComplete':PyJs_anonymous_13_,'isConsonant':PyJs_anonymous_14_,'isVowel':PyJs_anonymous_15_,'isCho':PyJs_anonymous_16_,'isJong':PyJs_anonymous_17_,'isHangulAll':PyJs_anonymous_18_,'isCompleteAll':PyJs_anonymous_19_,'isConsonantAll':PyJs_anonymous_20_,'isVowelAll':PyJs_anonymous_21_,'isChoAll':PyJs_anonymous_22_,'isJongAll':PyJs_anonymous_23_})
var.put('hangul', PyJs_Object_11_)
if ((var.get('define',throw=False).typeof()==Js('function')) and var.get('define').get('amd')):
    @Js
    def PyJs_anonymous_24_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return var.get('hangul')
    PyJs_anonymous_24_._set_name('anonymous')
    var.get('define')(PyJs_anonymous_24_)
else:
    if PyJsStrictNeq(var.get('module',throw=False).typeof(),Js('undefined')):
        var.get('module').put('exports', var.get('hangul'))
    else:
        pass
pass


# Add lib to the module scope
hangul = var.to_python()