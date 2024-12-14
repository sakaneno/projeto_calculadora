import pyautogui
def divisao(a,b):
    try:
        divisao = a/b
        return divisao
    except ZeroDivisionError:
        pyautogui.alert("Não é possível dividir!")