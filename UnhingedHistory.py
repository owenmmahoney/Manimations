import manim as m
Scene = m.Scene

class Intro(Scene):
    def construct(self):
        
        longino_color = m.ManimColor("#F8E0AD")
        longino_py = m.ImageMobject(r"assets/longino-pyramid.png")
        longino_py_svg = m.SVGMobject(r"assets/longisvg.svg").scale(1.25)
        longino_py.match_height(longino_py_svg)
        longino_py.match_height(longino_py_svg)
        longino_py_svg.move_to(m.ORIGIN)
        longino_py_svg.move_to(m.RIGHT * 3.0)
        longino_py.move_to(m.ORIGIN)
        longino_py.move_to(m.RIGHT * 3.0)
        text = m.Text("Longino Films", font_size=85, font="Times New Roman", color=longino_color)
        text.move_to(m.ORIGIN)
        peak = m.Text("so peak", font_size=35, font="Times New Roman", color=longino_color)
        text.next_to(longino_py, m.LEFT, buff=0.75)
        longino_py.set_z_index(30)

        self.wait(0.5)

        self.play(
            m.DrawBorderThenFill(longino_py_svg),
            m.Write(text, lag_ratio=0.05),
            run_time=3
        )

        self.wait(1.5)

        intro_group = m.Group(text, longino_py_svg)
        
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

        lf = m.Text("Longino Films Presents:", font_size=60, font="Times New Roman", color=(longino_color))
        written_by = m.Text("A Film Written By:\nOwen Mahoney & Bennett Rogers", font_size=60, font="Times New Roman", color=(longino_color))
        featuring = m.Text("Featuring Special Guest Stars: ", font_size=60, font="Times New Roman", color=(longino_color))
        slb = m.Text("Steven Lucas Bentley", font_size=60, font="Times New Roman", color=(longino_color))
        agk = m.Text("as Ghenghis Khan", font_size=45, font="Times New Roman", color=(longino_color))
        a = m.Text("&", font_size=60, font="Times New Roman", color=(longino_color))
        fgen4runnerimb = m.Text("First Gen 4Runner in Medium Blue", font_size=60, font="Times New Roman", color=(longino_color))
        asfgen4runnerimb = m.Text("as First Gen 4Runner in Medium Blue", font_size=45, font="Times New Roman", color=(longino_color))

        lf.move_to(m.ORIGIN)
        
        self.play(
            m.Write(lf),
            run_time=2.75
        )

        self.wait(2)

        written_by.move_to(m.ORIGIN)

        self.play(
            m.ReplacementTransform(lf, written_by),
            run_time=1.5
        )

        self.wait(2)

        featuring.move_to(m.ORIGIN)

        self.play(
            m.ReplacementTransform(written_by, featuring),
            run_time=1.5
        )

        self.wait(2)

        slb.move_to(m.ORIGIN, m.UP*3)
        agk.next_to(slb, m.DOWN, buff=0.5)
        slbagk = m.VGroup(slb, agk)
        slbagk.move_to(m.UP*0.25)

        self.play(
            m.ReplacementTransform(featuring, slbagk),
            run_time=1.5
        )

        self.wait(2)

        a.move_to(m.ORIGIN)

        self.play(
            m.ReplacementTransform(slbagk, a),
            run_time=1.5
        )

        self.wait(2)

        fgen4runnerimb.move_to(m.ORIGIN, m.UP*3)
        asfgen4runnerimb.next_to(fgen4runnerimb, m.DOWN, buff=0.5)
        fg4r = m.VGroup(fgen4runnerimb, asfgen4runnerimb)
        fg4r.move_to(m.UP*0.25)

        self.play(
            m.ReplacementTransform(a, fg4r),
            run_time=1.5
        )

        self.wait(2)

        self.play(
            m.FadeOut(fg4r),
            run_time=2
        )

class Test(Scene):
    def construct(self):

        longino_py = m.ImageMobject(r"assets/longino-pyramid.png")
        longino_py_svg = m.SVGMobject(r"assets/longisvg.svg").scale(1.25)
        longino_py.match_height(longino_py_svg)
        longino_py.match_height(longino_py_svg)
        
        self.play(
            m.DrawBorderThenFill(longino_py_svg),
            run_time=3
        )

        self.play(
            m.FadeTransform(longino_py_svg, longino_py),
            run_time=2
        )
        
class Outro(Scene):
    def construct(self):
        
        toyotal = m.SVGMobject(r"assets\toyota-logo.svg").scale(1.5).set_color(m.WHITE)
        toyota = m.Text("Team Toyota Wins!", font_size=40)
        toyotal.move_to(m.ORIGIN)
        toyota.next_to(toyotal, m.DOWN, buff=0.25)
        
        self.play(
            m.DrawBorderThenFill(toyotal),
            m.Write(toyota),
            run_time=3
        )