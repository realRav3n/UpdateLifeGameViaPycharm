import uiFunction
import Global

ui = uiFunction.uiFunction()

scr = ui.init((1600, 900), "Test")
la1 = ui.label(30, (120, 30), "freesansbold.ttf", Global.white,
               Global.grey, "Life Game")
bu1 = ui.button(30, (80, 200), "freesansbold.ttf", Global.white,
                Global.grey, Global.white, Global.grey, title="start")

bu2 = ui.button(30, (80, 400), "freesansbold.ttf", Global.white,
                Global.grey, Global.white, Global.grey, title="pause")

bu3 = ui.button(30, (80, 600), "freesansbold.ttf", Global.white,
                Global.grey, Global.white, Global.grey, title="reset")

bu4 = ui.button(30, (80, 800), "freesansbold.ttf", Global.white,
                Global.grey, Global.white, Global.grey, title="random")



if __name__ == '__main__':
    ui.register_cp(la1)
    ui.register_cp(bu1)
    ui.register_cp(bu2)
    ui.register_cp(bu3)
    ui.register_cp(bu4)
    ui.run(scr, (0, 0, 0))
