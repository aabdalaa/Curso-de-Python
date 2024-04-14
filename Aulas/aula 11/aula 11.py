from time import sleep
from os import startfile
a = 0

while True:
    nome = str(input('digite o nome de um personagem de undertale: ').lower()).strip()
    print('---' * 50)

    if nome == 'aaaaaa':
        print('Não é muito criativo... ?')

    elif nome == 'fight':
        print('Isso é um pouco irritante, não é ...?')
        startfile('chara.mp3')

    elif nome == 'mercy':
        print('Isso é um pouco irritante, não é ...?')
        startfile('chara.mp3')

    elif nome == 'chara':
        print('O verdadeiro nome.')
        startfile('chara.mp3')

    elif nome == 'frisk':
        sip = str(input('Atenção: esse nome vai tornar a sua vida um inferno. Continuar assim mesmo[S/N]? ')).upper()
        if sip == 'S':
            startfile('chara.mp3')
        if sip == 'N':
            print('')

    elif nome == 'temmie':
        print('hOI!')


    elif nome == 'catty':
        print('Malcriado! Malcriado! Esse é o MEU nome!')


    elif nome == 'aaron':
        print('Este nome está correto?')


    elif nome == 'jerry':
        print('Jerry')


    elif nome == 'papyrus':
        print('VOU PERMITIR !!!!')
        startfile('papyrus.mp3')


    elif nome == 'papyru':
        print('VOU PERMITIR !!!!')
        startfile('papyrus.mp3')

    elif nome == 'alphy':
        print('Uh .... OK?')
        startfile('Alphys.mp3')

    elif nome == 'napstablook':
        print('............ (Eles são impotentes para pará-lo.)')
        startfile('napstablook.mp3')

    elif nome == 'napsta blooky':
        print('............ (Eles são impotentes para pará-lo.)')
        startfile('napstablook.mp3')

    elif nome == 'napstablooky':
        print('............ (Eles são impotentes para pará-lo.)')
        startfile('napstablook.mp3')

    elif nome == 'blooky':
        print('............ (Eles são impotentes para pará-lo.)')
        startfile('napstablook.mp3')

    elif nome == 'napsta':
        print('............ (Eles são impotentes para pará-lo.)')
        startfile('napstablook.mp3')

    elif nome == 'bpants':
        print('Você está realmente raspando o fundo do barril.')


    elif nome == 'burger pants':
        print('Você está realmente raspando o fundo do barril.')


    elif nome == 'burgerpants':
        print('Você está realmente raspando o fundo do barril.')


    elif nome == 'gerson':
        print('Wah ha ha! Por que não?')


    elif nome == 'shyren':
        print(' ...? ')


    elif nome == 'woshua':
        print('Nome limpo.')


    elif nome == 'bratty':
        print('Tipo, acho que sim.')


    elif nome == 'drak':
        print('O Bife na Forma do Rosto de Mettaton aparece como "FSteak" ao invés de "FaceSteak". Este nome é uma '
              'referência à história em quadrinhos Persona 4 do Gigidigi, "Hiimdaisy". Notavelmente, Gigidigi também '
              'ajudou a trabalhar no jogo.')
        startfile('steak_in_the_shape_of_mettaton_s_face_-4728384343908244879.mp3')

    elif nome == 'gigi':
        print('O Bife na Forma do Rosto de Mettaton aparece como "FSteak" ao invés de "FaceSteak". Este nome é uma '
              'referência à história em quadrinhos Persona 4 do Gigidigi, "Hiimdaisy". Notavelmente, Gigidigi também '
              'ajudou a trabalhar no jogo.')
        startfile('steak_in_the_shape_of_mettaton_s_face_-4728384343908244879.mp3')

    elif nome == 'gugu':
        print('O Bife na Forma do Rosto de Mettaton aparece como "FSteak" ao invés de "FaceSteak". Este nome é uma '
              'referência à história em quadrinhos Persona 4 do Gigidigi, "Hiimdaisy". Notavelmente, Gigidigi também '
              'ajudou a trabalhar no jogo.')
        startfile('steak_in_the_shape_of_mettaton_s_face_-4728384343908244879.mp3')

    elif nome == 'alphys':
        print('N -não faça isso.')
        startfile('Alphys.mp3')

    elif nome == 'asgore':
        print('Você não pode.')
        startfile('asgore.mp3')

    elif nome == 'asriel':
        print('...')
        startfile('asriel.mp3')

    elif nome == 'flowey':
        print('Eu já ESCOLHI esse nome.')
        startfile('flowey.mp3')

    elif nome == 'gaster':
        startfile('wd gaster.mp3')
        sleep(41)

    elif nome == 'toriel':
        print('Acho que você deveria pensar no seu próprio nome, meu filho.')
        startfile('toriel.mp3')

    elif nome == 'undyne':
        print('Obtenha seu PRÓPRIO nome !')
        startfile('undyne.mp3')

    elif nome == 'sans':
        print('não')
        startfile('sans.mp3')

    elif nome == 'dummy':
        print('fútil, fútil, fútil !')
        startfile('dummy.mp3')

    elif nome == 'boneco':
        print('fútil, fútil, fútil !')
        startfile('dummy.mp3')

    elif nome == 'boneco doido':
        print('fútil, fútil, fútil !')
        startfile('dummy.mp3')

    else:
        print('Esse nome não existe no mundo de Undertale ou talvez você não digitou corretamente !')

    if a == 0:
        print('---'*50)

    continuar = str(input('Deseja continuar[S/N]? ')).upper()
    if continuar == 'S':
        print('---'*50)
        continue
    if continuar == 'N':
        print('Obrigado pela participação do projeto !')
        break
