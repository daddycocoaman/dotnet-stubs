from typing import Tuple, Set, Iterable, List


class UnicodeRange(Object):
    def __init__(self, firstCodePoint: int, length: int): ...
    def Create(firstCharacter: Char, lastCharacter: Char) -> UnicodeRange: ...
    @property
    def FirstCodePoint(self) -> int: ...
    @property
    def Length(self) -> int: ...


class UnicodeRanges(Object):
    @property
    def All() -> UnicodeRange: ...
    @property
    def AlphabeticPresentationForms() -> UnicodeRange: ...
    @property
    def Arabic() -> UnicodeRange: ...
    @property
    def ArabicExtendedA() -> UnicodeRange: ...
    @property
    def ArabicPresentationFormsA() -> UnicodeRange: ...
    @property
    def ArabicPresentationFormsB() -> UnicodeRange: ...
    @property
    def ArabicSupplement() -> UnicodeRange: ...
    @property
    def Armenian() -> UnicodeRange: ...
    @property
    def Arrows() -> UnicodeRange: ...
    @property
    def Balinese() -> UnicodeRange: ...
    @property
    def Bamum() -> UnicodeRange: ...
    @property
    def BasicLatin() -> UnicodeRange: ...
    @property
    def Batak() -> UnicodeRange: ...
    @property
    def Bengali() -> UnicodeRange: ...
    @property
    def BlockElements() -> UnicodeRange: ...
    @property
    def Bopomofo() -> UnicodeRange: ...
    @property
    def BopomofoExtended() -> UnicodeRange: ...
    @property
    def BoxDrawing() -> UnicodeRange: ...
    @property
    def BraillePatterns() -> UnicodeRange: ...
    @property
    def Buginese() -> UnicodeRange: ...
    @property
    def Buhid() -> UnicodeRange: ...
    @property
    def Cham() -> UnicodeRange: ...
    @property
    def Cherokee() -> UnicodeRange: ...
    @property
    def CherokeeSupplement() -> UnicodeRange: ...
    @property
    def CjkCompatibility() -> UnicodeRange: ...
    @property
    def CjkCompatibilityForms() -> UnicodeRange: ...
    @property
    def CjkCompatibilityIdeographs() -> UnicodeRange: ...
    @property
    def CjkRadicalsSupplement() -> UnicodeRange: ...
    @property
    def CjkStrokes() -> UnicodeRange: ...
    @property
    def CjkSymbolsandPunctuation() -> UnicodeRange: ...
    @property
    def CjkUnifiedIdeographs() -> UnicodeRange: ...
    @property
    def CjkUnifiedIdeographsExtensionA() -> UnicodeRange: ...
    @property
    def CombiningDiacriticalMarks() -> UnicodeRange: ...
    @property
    def CombiningDiacriticalMarksExtended() -> UnicodeRange: ...
    @property
    def CombiningDiacriticalMarksforSymbols() -> UnicodeRange: ...
    @property
    def CombiningDiacriticalMarksSupplement() -> UnicodeRange: ...
    @property
    def CombiningHalfMarks() -> UnicodeRange: ...
    @property
    def CommonIndicNumberForms() -> UnicodeRange: ...
    @property
    def ControlPictures() -> UnicodeRange: ...
    @property
    def Coptic() -> UnicodeRange: ...
    @property
    def CurrencySymbols() -> UnicodeRange: ...
    @property
    def Cyrillic() -> UnicodeRange: ...
    @property
    def CyrillicExtendedA() -> UnicodeRange: ...
    @property
    def CyrillicExtendedB() -> UnicodeRange: ...
    @property
    def CyrillicExtendedC() -> UnicodeRange: ...
    @property
    def CyrillicSupplement() -> UnicodeRange: ...
    @property
    def Devanagari() -> UnicodeRange: ...
    @property
    def DevanagariExtended() -> UnicodeRange: ...
    @property
    def Dingbats() -> UnicodeRange: ...
    @property
    def EnclosedAlphanumerics() -> UnicodeRange: ...
    @property
    def EnclosedCjkLettersandMonths() -> UnicodeRange: ...
    @property
    def Ethiopic() -> UnicodeRange: ...
    @property
    def EthiopicExtended() -> UnicodeRange: ...
    @property
    def EthiopicExtendedA() -> UnicodeRange: ...
    @property
    def EthiopicSupplement() -> UnicodeRange: ...
    @property
    def GeneralPunctuation() -> UnicodeRange: ...
    @property
    def GeometricShapes() -> UnicodeRange: ...
    @property
    def Georgian() -> UnicodeRange: ...
    @property
    def GeorgianExtended() -> UnicodeRange: ...
    @property
    def GeorgianSupplement() -> UnicodeRange: ...
    @property
    def Glagolitic() -> UnicodeRange: ...
    @property
    def GreekandCoptic() -> UnicodeRange: ...
    @property
    def GreekExtended() -> UnicodeRange: ...
    @property
    def Gujarati() -> UnicodeRange: ...
    @property
    def Gurmukhi() -> UnicodeRange: ...
    @property
    def HalfwidthandFullwidthForms() -> UnicodeRange: ...
    @property
    def HangulCompatibilityJamo() -> UnicodeRange: ...
    @property
    def HangulJamo() -> UnicodeRange: ...
    @property
    def HangulJamoExtendedA() -> UnicodeRange: ...
    @property
    def HangulJamoExtendedB() -> UnicodeRange: ...
    @property
    def HangulSyllables() -> UnicodeRange: ...
    @property
    def Hanunoo() -> UnicodeRange: ...
    @property
    def Hebrew() -> UnicodeRange: ...
    @property
    def Hiragana() -> UnicodeRange: ...
    @property
    def IdeographicDescriptionCharacters() -> UnicodeRange: ...
    @property
    def IpaExtensions() -> UnicodeRange: ...
    @property
    def Javanese() -> UnicodeRange: ...
    @property
    def Kanbun() -> UnicodeRange: ...
    @property
    def KangxiRadicals() -> UnicodeRange: ...
    @property
    def Kannada() -> UnicodeRange: ...
    @property
    def Katakana() -> UnicodeRange: ...
    @property
    def KatakanaPhoneticExtensions() -> UnicodeRange: ...
    @property
    def KayahLi() -> UnicodeRange: ...
    @property
    def Khmer() -> UnicodeRange: ...
    @property
    def KhmerSymbols() -> UnicodeRange: ...
    @property
    def Lao() -> UnicodeRange: ...
    @property
    def Latin1Supplement() -> UnicodeRange: ...
    @property
    def LatinExtendedA() -> UnicodeRange: ...
    @property
    def LatinExtendedAdditional() -> UnicodeRange: ...
    @property
    def LatinExtendedB() -> UnicodeRange: ...
    @property
    def LatinExtendedC() -> UnicodeRange: ...
    @property
    def LatinExtendedD() -> UnicodeRange: ...
    @property
    def LatinExtendedE() -> UnicodeRange: ...
    @property
    def Lepcha() -> UnicodeRange: ...
    @property
    def LetterlikeSymbols() -> UnicodeRange: ...
    @property
    def Limbu() -> UnicodeRange: ...
    @property
    def Lisu() -> UnicodeRange: ...
    @property
    def Malayalam() -> UnicodeRange: ...
    @property
    def Mandaic() -> UnicodeRange: ...
    @property
    def MathematicalOperators() -> UnicodeRange: ...
    @property
    def MeeteiMayek() -> UnicodeRange: ...
    @property
    def MeeteiMayekExtensions() -> UnicodeRange: ...
    @property
    def MiscellaneousMathematicalSymbolsA() -> UnicodeRange: ...
    @property
    def MiscellaneousMathematicalSymbolsB() -> UnicodeRange: ...
    @property
    def MiscellaneousSymbols() -> UnicodeRange: ...
    @property
    def MiscellaneousSymbolsandArrows() -> UnicodeRange: ...
    @property
    def MiscellaneousTechnical() -> UnicodeRange: ...
    @property
    def ModifierToneLetters() -> UnicodeRange: ...
    @property
    def Mongolian() -> UnicodeRange: ...
    @property
    def Myanmar() -> UnicodeRange: ...
    @property
    def MyanmarExtendedA() -> UnicodeRange: ...
    @property
    def MyanmarExtendedB() -> UnicodeRange: ...
    @property
    def NewTaiLue() -> UnicodeRange: ...
    @property
    def NKo() -> UnicodeRange: ...
    @property
    def None() -> UnicodeRange: ...
    @property
    def NumberForms() -> UnicodeRange: ...
    @property
    def Ogham() -> UnicodeRange: ...
    @property
    def OlChiki() -> UnicodeRange: ...
    @property
    def OpticalCharacterRecognition() -> UnicodeRange: ...
    @property
    def Oriya() -> UnicodeRange: ...
    @property
    def Phagspa() -> UnicodeRange: ...
    @property
    def PhoneticExtensions() -> UnicodeRange: ...
    @property
    def PhoneticExtensionsSupplement() -> UnicodeRange: ...
    @property
    def Rejang() -> UnicodeRange: ...
    @property
    def Runic() -> UnicodeRange: ...
    @property
    def Samaritan() -> UnicodeRange: ...
    @property
    def Saurashtra() -> UnicodeRange: ...
    @property
    def Sinhala() -> UnicodeRange: ...
    @property
    def SmallFormVariants() -> UnicodeRange: ...
    @property
    def SpacingModifierLetters() -> UnicodeRange: ...
    @property
    def Specials() -> UnicodeRange: ...
    @property
    def Sundanese() -> UnicodeRange: ...
    @property
    def SundaneseSupplement() -> UnicodeRange: ...
    @property
    def SuperscriptsandSubscripts() -> UnicodeRange: ...
    @property
    def SupplementalArrowsA() -> UnicodeRange: ...
    @property
    def SupplementalArrowsB() -> UnicodeRange: ...
    @property
    def SupplementalMathematicalOperators() -> UnicodeRange: ...
    @property
    def SupplementalPunctuation() -> UnicodeRange: ...
    @property
    def SylotiNagri() -> UnicodeRange: ...
    @property
    def Syriac() -> UnicodeRange: ...
    @property
    def SyriacSupplement() -> UnicodeRange: ...
    @property
    def Tagalog() -> UnicodeRange: ...
    @property
    def Tagbanwa() -> UnicodeRange: ...
    @property
    def TaiLe() -> UnicodeRange: ...
    @property
    def TaiTham() -> UnicodeRange: ...
    @property
    def TaiViet() -> UnicodeRange: ...
    @property
    def Tamil() -> UnicodeRange: ...
    @property
    def Telugu() -> UnicodeRange: ...
    @property
    def Thaana() -> UnicodeRange: ...
    @property
    def Thai() -> UnicodeRange: ...
    @property
    def Tibetan() -> UnicodeRange: ...
    @property
    def Tifinagh() -> UnicodeRange: ...
    @property
    def UnifiedCanadianAboriginalSyllabics() -> UnicodeRange: ...
    @property
    def UnifiedCanadianAboriginalSyllabicsExtended() -> UnicodeRange: ...
    @property
    def Vai() -> UnicodeRange: ...
    @property
    def VariationSelectors() -> UnicodeRange: ...
    @property
    def VedicExtensions() -> UnicodeRange: ...
    @property
    def VerticalForms() -> UnicodeRange: ...
    @property
    def YijingHexagramSymbols() -> UnicodeRange: ...
    @property
    def YiRadicals() -> UnicodeRange: ...
    @property
    def YiSyllables() -> UnicodeRange: ...
