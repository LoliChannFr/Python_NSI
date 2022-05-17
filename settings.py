import pygame, os

levelmap=[  [ #le joueur voit par paquet de dix lignes
'WTTTTTTTT    TTTTTTTTTTTTTTTTTTTT',
'W       W    W                   ',
'W       W    W          W        ',
'W       W    W         GGGG      ',
'W       W    W                   ',
'W       W    W                   ',
'W       W    W                   ',
'W       W    W           Y       ',
'W P                      Y       ',
'W                        Y       ',
'',
'',
'',
'WGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'WGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG',
'',
'',
'',
'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS',
'B'],
['EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEGGGGGGGGGGGGGGEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEGGGGGGGGGGGGGGEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEGGGGGGGGGGGGGGEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEGGGGGGGGGGGGGGEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEETTTTTTTTTTTTTEETTTTTTTTTTTTTTTTTEEEEEEEEEEEETTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT',
'EEEEEEEEEEEEET             TT                 TTTEEEEEEETT                                                 WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEETT                                    TEEEETT             L                                     WWWWWWWWWWAAAAAAWWAAAAAAWWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEET                                       TEET              WWWW                                   WWWWWAAAAAAAAAAAAAAAAAAAAAAAAWWWWEEEEEEEEEEEEEEEEEEEEEEE',                                                                                                                
'EEEEEEEEEE                                         TT               W→                                      WWWAAAAAAAAVVAAAAAAVVAAAAAAAAWWWEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEG                                                         W→                                      WWAAAAAAAAAAAAAAAAAAAAAAAAAAAAWWEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEE                                                         W→                                      WWAAAAAAAAAAAAAAAAAAAAAAAAAAAAWWEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEG                                                        W→                    W      K          WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWEEEEEEEEEEEEEEEEEEEEEEE',
'WEEEEEEEEEEE                                                        W→                    W                 WAAAAA  AAAAAAA  AAAAAAA  AAAAAWEEEEEEEEEEEEEEEEEEEEEEE',
'WWEEEEEEEEEE         P                     W                        W→                    W    WUUW         W          AA      AA          WEEEEEEEEEEEEEEEEEEEEEEE',
'AWEEEEEEEEEEG                U             W                        W→             W   W  W                 D          AA      AA    F     WEEEEEEEEEEEEEEEEEEEEEEE',
'AWWEEEEEEEEEEG       L  U    U    A   L    W               L        W↑↑↑↑↑↑        W↑↑↑W↑↑W   ↑↑↑↑↑↑↑↑↑↑         L     AAM M M AA          WEEEEEEEEEEEEEEEEEEEEEEE',
'AAWWEEEEEEEEEEWGGGGGGGGGGGGGGEGGGGGGGGGGGGGEGGGGGGGEGGGGGGGGGGGGGGGGEGGGGGGGGGGGGGGEGGGEGGEGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGEEEEEEEEEEEEEEEEEEEEEEEE',
'AAAWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'WAAWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'WAAWWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEGGGGGGGGGGGGGGEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'WAAAWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'WAAAWWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEGGGGGGGGGGGGGGEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'   ',
'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS',
'B'],
['EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEETTTTTTTTTTTTTTTTTTTTTEEEEETTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT',
'EEEEEEEEEEU                     TTEET                           W        W                           U                                            ',
'EEEEEEEEEEU                       ET                         UUUWUUU     W                           U                                            ',
'EEEEEEEEEEU       GG     WWW      T                          D K K D     W                           U    W      UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU                                 ',                                                                                                                
'EEEEEEEEEEU           W  W                                    M          W       🚩        U          U    W                       ←U                 ',
'EEEEEEEEEEU           ↓  U                W         W        UUUUUUU     WWWWWWWUUUUUU         W          W                       ←U           K          ',
'EEEEEEEEEEUGGG          ←U                W   WW                W           D        U                    W                  U    ←U               ',
'EEEEEEEEEEUE   W   W     U                W                   K U                    UWW                  W   U                   ←U          UUU  ',
'EEEEEEEEEEU              U             W                 W      U        WWWWWWW                     U    W            UU         ←U                       ',
'EEEEEEEEEEU     P        U  WW                       W       WWWW                          U         U    W       U                      UU          ',
'EEEEEEEEEEU            GGG           W                                            UU    W  U         U    W                                       ',
'EEEEEEEEEEUU       ↑↑↑↑EEE↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑U↑↑↑↑↑↑↑↑↑U↑↑↑↑W↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑UUUUU↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑                                                                                                                          ',
'EEEEEEEEEEEEGGGGGGGGGGGEEEGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGEGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE                                            GGGGGGGGGGGGGG',
'   ',
'   ',
'   ',
'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS',
'B']   ]
levelsign = [[],
["Keep calm, but the spikes can kill you.","Press directional keys to move.","You can also make double jump.","As you can double jump, you can climb the walls.","Use your fucking gun to shoot the mobs."],
[]]


tile_size = 48

def import_folder(path):
    surface_list = []
    for _,__,img_files in os.walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list