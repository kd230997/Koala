#!/usr/bin/python

try:
    import sys
    import os
    import pygame
    import pygame.camera
    from pygame.locals import *
except err:
    print(f"couldn't load module. {err}")
    sys.exit(2)


class Capture:
    def __init__(self):
        pygame.camera.init()
        self.size = (640, 480)
        # create a display surface. standard pygame stuff
        self.display = pygame.display.set_mode(self.size, 0)

        # this is the same as what we saw before
        self.clist = pygame.camera.list_cameras()
        if not self.clist:
            raise ValueError("Sorry, no cameras detected.")
        self.cam = pygame.camera.Camera(self.clist[0], self.size)
        self.cam.start()

        # create a surface to capture to.  for performance purposes
        # bit depth is the same as that of the display surface.
        self.snapshot = pygame.surface.Surface(self.size, 0, self.display)

    def get_and_flip(self):
        # if you don't want to tie the framerate to the camera, you can check
        # if the camera has an image ready.  note that while this works
        # on most cameras, some will never return true.
        if self.cam.query_image():
            self.snapshot = self.cam.get_image(self.snapshot)

        # blit it to the display surface.  simple!
        self.display.blit(self.snapshot, (0, 0))

    def main(self):
        going = True
        font = pygame.font.Font(None, 36)

        count = 0
        image = pygame.image.load(os.path.join("assets", "wizard", "stand.png"))
        while going:
            events = pygame.event.get()
            for e in events:
                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                    # close the camera safely
                    self.cam.stop()
                    going = False
                    sys.exit()

                if e.type == KEYDOWN:
                    if e.key == K_SPACE:
                        count += 1
                        break
                    if e.key == K_r:
                        count = 0
                        break

            text_surface = font.render(f"Count: {count}", True, (255, 255, 255))

            self.get_and_flip()
            self.display.blit(text_surface, (10, 10))
            self.display.blit(image, (540, 10))

            pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    capture = Capture()

    capture.main()
    pygame.quit()
