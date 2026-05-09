import manim as m
Scene = m.Scene
m.config.disable_caching = True

class Max_Goodman(Scene):
    def construct(self):


            Max = m.ImageMobject(r"assets\max-transparent.png")
            Saul_Goodman = m.ImageMobject(r"assets\saul-goodman3d.gif")
            Max.scale(2.5)
            Saul_Goodman.scale(3)

            self.add_sound(r"assets\boing_lmke36X.wav", time_offset=0.5)
            self.play(m.FadeIn(Max, scale=0.5))
            self.wait(2)

            self.add_sound(r"assets\saul-goodman-short.wav")
            self.play(m.FadeTransform(Max, Saul_Goodman))
            self.wait(0.55)

            self.play(m.FadeOut(Saul_Goodman))