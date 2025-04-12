
# TTS Converter

## Introduction
The TTS Converter is a Python-based program that converts text into speech. It provides a graphical user interface (GUI) where users can enter text, choose between male or female voices, and save the speech as an MP3 file.

## Dependencies
- **pyttsx3**: Python library for text-to-speech conversion.
- **Tkinter**: Python GUI library to build the interface.

## How It Works
The program initializes a Tkinter window with fields to input text, select the desired voice, and specify the output filename. Upon clicking the "Convert to Speech" button:
1. The program reads the text input from the user.
2. The text is passed to the `pyttsx3` engine, which converts the text to speech.
3. The resulting speech is saved as an MP3 file.

### Components
1. **Text Input**: A large text box where the user can type the text to be converted to speech.
2. **Voice Selection**: Radio buttons that allow the user to choose between male and female voices.
3. **Filename Input**: A field where the user can enter the desired name for the MP3 file (without extension).
4. **Convert Button**: Once clicked, it triggers the conversion process, saving the speech file.

## Error Handling
- If no text is provided, the program shows an error message asking the user to enter some text.
- If no filename is provided, it defaults to "output.mp3".

## Customization
- The speech rate and volume can be customized by modifying the `engine.setProperty` methods.
- The available voices depend on the system's TTS engine, but you can adjust them based on the available voice IDs.

## Example

1. Text: `Hello, welcome to the TTS Converter.`
2. Filename: `greeting`
3. Result: The speech will be saved as `greeting.mp3`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, feel free to open an issue on the [GitHub repository](https://github.com/mavilinux/tts-converter).
