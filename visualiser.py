import sortalgos, time, os, sys
os.environ['PYGAME_HIDE__SUPPORT_PROMPT'] = "hide"
import pygame

dimensions = (1024,512)
algorithms = {"SelectionS": sortalgos.SelectionS(), \
              "BubbleS": sortalgos.BubbleS(), \
              "InsertionS": sortalgos.InsertionS(), \
              "ShellS": sortalgos.ShellS(), \
              "QuickS": sortalgos.QuickS(), \
              "MergeS": sortalgos.MergeS(), \
              "HeapS": sortalgos.HeapS(), \
              "BucketS": sortalgos.BucketS(), \
              "RadixS": sortalgos.RadixS()}

if len(sys.argv) > 1:
    if sys.argv[1] == "list":
        for key in algorithms.keys(): print(key, end=" ")
        print("")
        sys.exit(0)

# Pygame Initialisation
pygame.init()
display = pygame.display.set_mode((dimensions[0], dimensions[1]))
display.fill(pygame.Color("white"))

# Plays a sound if you are on Ubuntu/Debian
# First install sox with: sudo apt install sox
# Note: This makes the program a lot slower
def play_sound(swap):
    duration = 0.01
    freq = 20
    os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq+swap*10))

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();

def update(algorithm, swap1=None, swap2=None, display=display):
    display.fill(pygame.Color("white"))
    pygame.display.set_caption("Sorting Visiualiser     Algorithm: {}     Time: {:.3f}      Status: Sorting".format(algorithm.name, time.time() - algorithm.start_time))
    k = int(dimensions[0]/len(algorithm.array))
    for i in range(len(algorithm.array)):
        colour = (0,0,0)
        if swap1 == algorithm.array[i]:
            colour = (0,255,0)
        elif swap2 == algorithm.array[i]:
            colour = (255,0,0)
        pygame.draw.rect(display, colour, (i*k,dimensions[1],k,-algorithm.array[i]))
    #play_sound(swap2) # - Uncomment if you want sound to play with each swap
    check_events()
    pygame.display.update()

def keep_open(algorithm, display, time):
    pygame.display.set_caption("Sorting Visiualiser     Algorithm: {}     Time: {:.3f}      Status: Done".format(algorithm.name, time))
    while True:
        check_events()
        pygame.display.update()

def main():
    if len(sys.argv) < 2:
        print("Error: Enter a sorting algorithm")
    else:
        try:
            algorithm = algorithms[sys.argv[1]]
            try:
                time_elapsed = algorithm.run()[1]
                keep_open(algorithm, display, time_elapsed)
                pass
            except:
                pass
        except:
            print("Error: {} is not a valid sorting algorithm".format(sys.argv[1]))
            print("Note: Sorting algorithms are in Camel Case")

if __name__ == "__main__":
    main()
