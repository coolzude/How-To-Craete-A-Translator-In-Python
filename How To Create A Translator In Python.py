from googletrans import Translator


# Variable
var1 = input('what is The Current Language You Choose ? : ')
var2 = input('words ? : ')
var3 = input('which is The Translated Language ? : ')


# Googletrans
Translation = Translator.translate(Translator(), src=var1, dest=var3, text=var2)
print(Translation.text)
