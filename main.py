# imortar las funciones aca
from envolvente import envolvente
from read_wav import read_wav
from get_files_paths import get_files_paths
from find_syllables import find_syllables
from split_syllables import split_syllables
from spectrum import spectrum

def main():
    audios = get_files_paths()
    envelope = envolvente()
    spectre = s1pectrum()


if __name__ == "__main__":
   main()
