import manim as m
Scene = m.Scene

class TeslaCC(Scene):
    def construct(self):

        self.camera.background_color = m.WHITE
 
 
             
        tesla_path = r"C:\Users\owenmmahoney\Downloads\icons\tesla-coil.png" 
        tesla_img = m.ImageMobject(tesla_path)
        tesla_img.height = 5.0
        tesla_caption = m.Text("Nikola Tesla", font_size=37.5, color=m.BLACK)
        tesla_caption.next_to(tesla_img, m.DOWN, buff=0.5) 

    
        self.play(
            m.FadeIn(tesla_img, scale=0.8),
            m.FadeIn(tesla_caption, scale=0.8), 
        )

        self.wait(3.0)
        
        self.play(
            m.FadeOut(tesla_img, scale=1.2),
            m.FadeOut(tesla_caption, scale=1.2),
            run_time=1.0
        )

        icon_paths = {
            "Peculiar Habits": r"C:\Users\owenmmahoney\Downloads\icons\question-mark.png",
            "Entertaining":    r"C:\Users\owenmmahoney\Downloads\icons\drama-masks.png",
            "Curious":         r"C:\Users\owenmmahoney\Downloads\icons\magnifying-glass.png",
            "Disciplined":      r"C:\Users\owenmmahoney\Downloads\icons\hammer.png",
            "Imagination":     r"C:\Users\owenmmahoney\Downloads\icons\brain-gears.png",
            "Memory":          r"C:\Users\owenmmahoney\Downloads\icons\photograph.png",
            "Multilingual":    r"C:\Users\owenmmahoney\Downloads\icons\google-translate.png",
            "Bright":          r"C:\Users\owenmmahoney\Downloads\icons\lightbulb.png",
            "Not-greedy":         r"C:\Users\owenmmahoney\Downloads\icons\no-money-bag.png",
            "Futuristic":      r"C:\Users\owenmmahoney\Downloads\icons\rocketship.png",
        }

        for path in icon_paths.values():
            img = m.ImageMobject(path)
            img.height = 5.0
            
            self.play(m.FadeIn(img, scale=0.8), run_time=0.6)
            
            self.wait(1.5)
            
            self.play(m.FadeOut(img, scale=1.2), run_time=0.4)

        self.wait(1)
        