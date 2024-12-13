import pygame
import matplotlib
import numpy as np
from Aesthetics import *
from Aesthetics import Dropdown

width = 900
length = 700

pygame.font.init()
pygame.mixer.init()
pygame.display.init()
win = pygame.display.set_mode((width, length))

'''
GLOBAL VARIABLES
'''
buttons_list = [Buttons(0, length-100, width/4, 100, "Map Location", (255, 255, 255), "Map.png"),Buttons(width/4, length-100, width/4, 100, "Exercise", (255, 255, 255), "Exercise.png"),Buttons(width/2, length-100, width/4, 100, "Nutrition", (255, 255, 255), "Nutrition.png"),Buttons(3*width/4, length-100, width/4, 100, "Contacts", (255, 255, 255), "contacts.png")]
my_info_button_list = [Buttons(500, 200, 200, 100, "My Info", (128,0,0), "Nothing")]



class PetInformation:
    def __init__(self, name, age, weight, type, breed, xp, nutrition_database_fn, exercise_database_fn, nutritional_requirements, exercise_requirements, update_button):
        self.set_name(name)
        self.set_age(age)
        self.set_weight(weight)
        self.set_type(type)
        self.set_breed(breed)
        self.set_xp(xp)
        self.set_nutritional_database_fn(nutrition_database_fn)
        self.set_exercise_database_fn(exercise_database_fn)
        self.set_nutritional_requirements(nutritional_requirements)
        self.set_nutritional_requirements(exercise_requirements)
        self.set_update_button(update_button)
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def get_weight(self):
        return self._weight
    def get_type(self):
        return self._type
    def get_breed(self):
        return self._breed
    def get_xp(self):
        return self._xp
    def get_nutrition_database_fn(self):
        return self._nutritional_database_fn
    def get_exercise_database_fn(self):
        return self._exercise_database_fn
    def get_nutritional_requirements(self):
        return self._nutritional_requirements
    def get_exercise_requirements(self):
        return self._exercise_requirements
    def get_update_button(self):
        return self._update_button
    def set_name(self, name):
        self._name = name
    def set_age(self, age):
        self._age = age
    def set_weight(self, weight):
        self._weight = weight
    def set_type(self, type):
        self._type = type
    def set_breed(self, breed):
        self._breed = breed
    def set_xp(self, xp):
        self._xp = xp
    def set_nutritional_database_fn(self, nutritional_database_fn):
        self._nutritional_database_fn = nutritional_database_fn
    def set_exercise_database_fn(self, exercise_database_fn):
        self._exercise_database_fn = exercise_database_fn
    def set_nutritional_requirements(self, nutritional_requirements):
        self._nutritional_requirements = nutritional_requirements
    def set_exercise_requirements(self, exercise_requirements):
        self._exercise_requirements = exercise_requirements
    def set_update_button(self, update_button):
        self._update_button = update_button

pets_list = [PetInformation("Rocky", 16, 0, 0, 0, 0, 0, 0, 0, 0, Buttons(0, 0, 0, 0, "h", (0,0,0), "Nothing"))]

def home_screen():
    font = pygame.font.SysFont("Comic Sans MS", 30)
    text = font.render("hi", False, (0, 0, 0))
    win.blit(text, (500, 500))
    for i in buttons_list:
        i.draw(win)
    for i in my_info_button_list:
        i.draw(win)

def nutrition_screen():
    for i in buttons_list:
        i.draw(win)

def exercise_screen():
    for i in buttons_list:
        i.draw(win)
    dropdown = Dropdown(500, 500, 100, 100, [i.get_name() for i in pets_list], "Comic Sans MS")
    dropdown.draw(win)

def contacts_screen():
    for i in buttons_list:
        i.draw(win)

def my_info_screen():
    font = pygame.font.SysFont("Comic Sans MS", 30)
    for i in buttons_list:
        i.draw(win)
    text = font.render("My Info", False, (0,0,0))
    win.blit(text, ((width- text.get_width())/2, 10))
    text = font.render("Current Pets", False, (0, 0, 0))
    win.blit(text, (10, 50))
    for i in range(len(pets_list)):
        j = pets_list[i]
        pygame.draw.rect(win, (255, 255, 255), (0, 100*i+200, width, 10))
        text = font.render(j.get_name(), False, (0,0,0))
        win.blit(text, (100, 100*i+200))
        j.get_update_button().draw(win)
        text = font.render("Level: {}".format(j.get_xp()), False, (0,0,0))
        win.blit(text, (500, 100 * i+200))
        pygame.draw.rect(win, (255, 255, 255), (0, width, 100, 5))



def main():
    run = True
    function_being_run = ""
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button in buttons_list:
                    if button.click(mouse_pos):
                        if button.text == "Map Location":
                            function_being_run = "Home"
                        elif button.text == "Exercises":
                            function_being_run = "Exercises"
                        elif button.text == "Nutrition":
                            function_being_run = "Nutrition"
                        else:
                            function_being_run = "Contacts"
                for button in my_info_button_list:
                    if button.click(mouse_pos):
                        if button.text == "My Info":
                            function_being_run = "My Info"

        win.fill((255, 255, 255))
        if function_being_run == "Home" or function_being_run == "":
            home_screen()
        elif function_being_run == "Exercises":
            exercise_screen()
        elif function_being_run == "Nutrition":
            nutrition_screen()
        elif function_being_run == "Contacts":
            contacts_screen()
        elif function_being_run == "My Info":
            my_info_screen()
        pygame.display.update()
    pygame.quit()

main()