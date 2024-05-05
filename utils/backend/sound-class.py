###################### SOUND CLASS ################
# Citation: Song class
# built upon code from cmu 112 Advanced Animations with Tkinter https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#imageMethods    

class Song(object):
    def __init__(self, path):
        self.path = path
        self.process = None
        self.loop = False

        # Cuantitative properties
        # y is the time series: the audio signal represented as a one-dimensional numpy.ndarray
        # sr is the sample rate (number of samples per second)
        self.y, self.sr = librosa.load(self.path)
        self.tempo, self.beat_frames = librosa.beat.beat_track(y = self.y,
                                                               sr = self.sr)

        

    def isPlaying(self): return (self.process is not None)
    
    def checkProcess(self):
        # This method is run inside a separate thread
        # so the main thread does not hang while this runs.
        while self.process is not None:
            if (self.process.poll() is not None): self.process = None
            else: time.sleep(0.2)

        if self.loop: self.start(loop=True)

            
    def start(self, loop=False):
        self.stop()
        self.loop = loop
        self.process = subprocess.Popen(['afplay', self.path])  
        threading.Thread(target=self.checkProcess).start()

        
    def stop(self):
        process = self.process
        self.loop = False
        self.process = None
        if (process is not None):
            try: process.kill()
            except: pass


    # ratio we multiply the tempo by
    def changeTempo(self, desiredBPM):
        # y is the time series: the audio signal represented as a one-dimensional numpy.ndarray
        #sr is the sample rate (number of samples per second)
        # y, sr = librosa.load('songs/' + filename)

        # ratio we want to multiply by:
        ratio = desiredBPM / self.tempo

        # create copies of original songs but altered in a different directory
        path = self.path.replace('originals', 'altered') # non-destructive, doesn't affect self.path
        
        # create temporary file
        wavfile.write(path, int(ratio*self.sr), self.y)
