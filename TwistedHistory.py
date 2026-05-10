import manim as m
Scene = m.Scene

class Intro(Scene):
    def construct(self):
        
        longino_color = m.ManimColor("#F8E0AD")
        longino_py = m.ImageMobject(r"assets/longino-pyramid.png").scale(0.875)
        longino_py_svg = m.SVGMobject(r"assets/longino-pyramid-svg.svg").scale(1.25)
        longino_py_svg.set_color(longino_color)
        longino_py_svg.move_to(m.ORIGIN)
        text = m.Text("Longino Films", font_size=85, font="Times New Roman", color=longino_color)
        text.move_to(m.ORIGIN)
        peak = m.Text("so peak", font_size=35, font="Times New Roman", color=longino_color)
        lf = m.Text("L F", font_size=100, font="Times New Roman", color=m.BLACK )

        self.wait(0.5)

        self.play(
            m.Write(longino_py_svg),
            run_time=2.5
        )

        self.wait(0.5)

        longino_py.move_to(longino_py_svg.get_center())

        self.play(
            m.FadeTransform(longino_py_svg, longino_py),
            run_time=2
        )


        self.play(
            longino_py.animate.move_to(m.RIGHT * 3.0),
            run_time=1.5,
            rate_func=m.smooth
        )

        text.next_to(longino_py, m.LEFT, buff=0.75)
        
        self.play(
            m.Write(text, lag_ratio=0.05),
            run_time=2.575
        )

        intro_group = m.Group(longino_py, text)

        self.wait(1.25)
        
        self.play(
            m.FadeOut(intro_group),
            run_time=2.5
        )

        peak.move_to(m.ORIGIN)

        self.play(
            m.Write(peak),
            run_time=1.75
        )

        self.play(
            m.FadeOut(peak),
            run_time=2.25
        )