import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from random import randint

def cria_audio(audio, mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save(audio)
    playsound(audio)

cria_audio("boas_vindas.mp3", "Escolha um número entre 1 a 5")

recon = sr.Recognizer()

with sr.Microphone() as source:
    print("Diga alguma coisa")
    audio = recon.listen(source)

numero = int(recon.recognize_google(audio, language="pt-br"))

resultado = randint(1, 10)

print("Número sorteado foi ",resultado)

if numero == resultado:
    cria_audio("venceu.mp3", "Parabéns. Você acertou o número. Tente jogar na mega sena")
else:
    cria_audio("perdeu.mp3", "Infelizmente você errou. Tente novamente")