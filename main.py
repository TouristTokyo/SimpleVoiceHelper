from gtts import gTTS
import os
from playsound import playsound
import speech_recognition as sr


def main():
    while True:
        try:
            command = listen_command()
            do_command(command)
        except KeyboardInterrupt:
            exit()


def enter_command():
    return input("Введите команду: ")


def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите что-нибудь!")
        audio = r.listen(source, phrase_time_limit=5)

    # recognize speech using Sphinx
    try:
        text = r.recognize_google(audio, language='ru')
        print("Вы сказали:", text)
        return text
    except sr.UnknownValueError:
        print("Ассистент не понял, что вы сказали")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def do_command(command):
    if command is None:
        say_message("Я вас не понял")
        return
    message = command.lower()
    if message == "привет":
        say_message("Привет друг!")
    elif message == "пока":
        say_message("До новых встреч!")
        exit()
    else:
        say_message("Упс..\nЯ такого ещё не знаю")


def say_message(message):
    voice = gTTS(message, lang="ru")
    file = "audio.mp3"
    voice.save(file)
    playsound(file)
    print("Голосовой ассистент: " + message)
    os.remove(file)


if __name__ == '__main__':
    main()
