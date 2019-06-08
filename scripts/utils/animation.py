class Animation:

    def __init__(self, animation_frames, delay):
        self.frames = animation_frames
        self.delay = delay
        self.counter = 0
        self.current_frame = 0
        self.num_loops = 0        

    def update(self, dt):
        self.counter += dt * 1000
        if self.counter >= self.delay:
            self.counter = 0
            self.current_frame += 1
            if self.current_frame >= len(self.frames):
                self.current_frame = 0
                self.num_loops += 1

    def get_num_loops(self):
        return self.num_loops

    def get_frame(self):
        return self.frames[self.current_frame]

    def is_on_last_frame(self):
        return self.current_frame == len(self.frames) - 1