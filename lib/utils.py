#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def assert_msg(pred, msg = ""):
    if not pred:
        print msg
        exit(-1)

def print_him():
    him = u'''

                            //+osyssosooo+//
                      ::/ohmNNNNNNNNNNNNNNNNmdyo/
                     /ydNNNNmmNmmmdddddddhhddddNmdy+
                   /hNNNNmmddmddyyyssyyysssyyyhhshddho
                  sNNNNNmmddhysso+/:::/:::-://+sooyyyhd+:
                 hMNNmdhhyyo+//::---...........--/+sysymh:
                hMMNmhyoo++/    ---               -:oyshmh
               hMMMNmyo+oo+/:::---.......```````...-:+shmNo.
              +MMMMNmyoosso+::----....`.`````````...-/ohmNm
              dMMMMNmyssyso+::---..........```````...:+hNNm
              mMMMMNmyyyyso+:::--..`.......``````....-+yNMh
              yMMMMNmdhyyyyso++//:-....`--.....`....-:+dNMo
               mMMMMNdhhmdhso+///:/++:.`/s+++/:::/++:-+mMN.
              `+mNNNmNdNdyyyyyyys+/-+myddo+oso/-....shdNm/
               +hhddhyymsyyss+++-+sshNhN+:osoo///-..-N/+y.
               :hyyhhyydo+//::::--/hN+.-h-:/:-......-h../
               .ysyyyyyys+//-....:hms-.`:y:-:--.....//-..
                +yhyyyyyyysoooo+shyys-.`.:s/+//::://:...
                .ysyyyyhys/:--./syhmds+:os::///:--..-.
                `+syyyyhhyyo///+osssso/....``.:::----.
                ``-yyyyyyysososo+/:-...````...-::--...`
                  `yyyhyyy+:shdhysoo+/:----:::--....-`
                   +yyhhhys/:yhhhyysoo++++:...-....-.
                   .yyyhhhys//ooo+/:::--..```.     -`
                   smyyhhhdhy//s+/::---.......-:::-`
                 .yMMsyhhhdddho+o/:--...``...-::-.
               .+NMMMMyohhhddddhyss+///::--:///:.
          .+hmMMMMMMMMMm//shhdddddhhhhdhyso+//:-o+:-`
       -odMMMMMMMMMMMMMMMy--/oyhhyyyyysso+++/:.-NNNNNmhs/-`
   ./smNNNNMMMMMMMMMMMMMMMm+-..-/osssso/::-.`  -NNNNNNNNNNNds/-`
sdNNNNNNNNNNMMMMMMMMMMMMMMMMs..````.:/+/:.`    /NNNNNNNNNNNNNNNNds+-
NNNNNNNNNNNNNNMMMMMMMMMMMMMMNs``   .+sysyyy+`  sNNNNNNNNNNNNNNNNNNNNNho:`
NNNNNNNNNNNNNNNMMMMMMMMMMMMMNNy` `odhdyyosydh. :NNNNNNNNNNNNNNNNNNNNNNNNNh+
NNNNNNNNNNNNNNNMMMMMMMMMMMMMNNNd.oyydmdhysh++o..mNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNMMMMMMMMMMNNNNNNNm.-/-sdmdys   `-yNNNNNNNNNNNNNNNNNNNNNNNNNN    '''
    print him

    print u"来自长者的凝视..."
    raw_input(u"按任意键继续...\n".encode(sys.stdout.encoding))
    return