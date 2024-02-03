# main.py to manipulate the window
# color or screen colour in kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# BoxLayout arranges children in a vertical or horizontal box.
# or help to put the childrens at the desired location.
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
Builder.load_string('''  
# Multiple_Slider.kv file of the main.py file.

#.kv file to manipulate the window colour.
<MultipleSliderWidget>:

    # giving the orientation of Slider
    orientation: "vertical"

    # initially providing this colour to window
    slider_colors: 0.5, 0.5, 0.5

    # executed before the canvas group.
    canvas.before:
        Color:
            rgb: root.slider_colors
        Rectangle:
            pos: root.pos
            size: root.size

    # creating the Slider
    Slider:
        min: 0  # minimum value of Slider
        max: 1 # maximum value of Slider
        value: 0.5  # initial value of Slider

        # when slider moves then to increase value
        on_value: root.slider_colors[0] = self.value;
    Slider:
        min: 0
        max: 1
        value: 0.5
        on_value: root.slider_colors[1] = self.value

    Slider:
        min: 0
        max: 1
        value: 0.5
        on_value: root.slider_colors[2] = self.value

    # Adding The label
    Label:
        font_size: "30sp"
        # the for loop is for continuously changing
        # the colour as slider value changes
        text: "Color:" + ", ".join(["%.3f" %(i) for i in root.slider_colors])
        color: 0, 0, 1, 1
''')

# creating the root widget used in .kv file
class MultipleSliderWidget(BoxLayout):
	pass


# class in which name .kv file must be named Slider.kv.
# or creating the App class
class Multiple_Slider(App):
	def build(self):
		# returning the instance of SliderWidget class
		return MultipleSliderWidget()


# run the app
if __name__ == '__main__':
	Multiple_Slider().run()
