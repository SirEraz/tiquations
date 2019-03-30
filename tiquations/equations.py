#Package created by Tinos Psomadakis
#Version 0.0.9
import webbrowser
import os
import math
from .constants import *

def version():
    print('''
Currently running Version tiquations 0.0.9
Changelog:
-Removed units and prints to help make equations easier to implement into code. Answers will now be returned rather than printed.
-Bug fixes
-Typo fixes
-Added power, energy, time equations.
-Added cosine rule equations
-Added euler's constants to constants
-Added Golden ration to constants
-Added Orbital speed, orbital time, radius equations.

''')

#Quadratic formula solver
def quadratic(num1,num2,num3):
    result1 = (-num2 + math.sqrt(num2**2 - (4 * (num1) * (num3))))
    ans1 = (result1 / (2 * num1))
    result2 = (-num2 - math.sqrt(num2**2 - 4 * (num1) * (num3)))
    ans2 = (result2 / (2 * num1))
    return ans1, ans2


#Solve distance using speed and time
def distance_dst(speed, time):
    return speed*time

#Solve speed using distance and time
def speed_dst(distance, time):
    return distance/time

#Solve time using speed and distance
def time_dst(distance, speed):
    return distance/speed

#Solve force using mass and acceleration
def force_fma(mass,acceleration):
    return mass*acceleration


#Solve mass using force and acceleration
def mass_fma(force,acceleration):
    return force/acceleration


#Solve acceleration using mass and force
def acceleration_fma(force,mass):
    return force/mass


#Solve weight using mass and gravitational field strength
def weight_wmg(mass, gravitational_field_strength):
    return mass*gravitational_field_strength

    
#Solve mass using weight and gravitational field strength
def mass_wmg(weight, gravitational_field_strength):
    return weight/gravitational_field_strength


#Solve gravitational field strength using weight and mass
def gravity_wmg(weight, mass):
    return weight/mass


#Solve for area of circle using radius
def circle_area_rad(radius):
    return pi*(radius**2)

    
#Solve for area of circle using diameter
def circle_area_dia(diameter):
    return (1/4)*(pi*(diameter**2))

    
#Solve for diameter of circle using radius
def circle_diam_rad(radius):
    return radius*2

    
#Solve for diameter of circle using area
def circle_diam_are(area):
    return 2*(math.sqrt(area/pi))

    
#Solve for circumference of circle using area
def circle_circum(radius):
    return 2*(pi*radius)


#Solve acceleration using Change in velocity and time
def acceleration_avt(delta_velocity,time):
    return delta_velocity/time

    
#Solve Change in velocity using acceleration and time
def delta_velocity_avt(acceleration,time):
    return acceleration*time

    
#Solve time taken using acceleration and change in velocity
def time_avt(acceleration,delta_velocity):
    return delta_velocity/acceleration


#Solve pressure using force and area
def pressure_fpa(force, area):
    return force/area


#Solve force using pressure and area
def force_fpa(pressure, area):
    return pressure/area

    
#Solve area using pressure and force
def area_fpa(force, pressure):
    return force*pressure

    
#Solve volume of a cylinder
def cylinder_vol(radius,height):
    return pi*(radius**2*(height))

    
#Solve surface area of a cylinder
def cylinder_surface_are(radius,height):
    return (2*(pi*radius*height))+2*(pi*(radius**2))

    
#Solve area of a trapezoid
def trapezoid_area(base_short,base_long,height):
    return ((base_short+base_long)/2)*height

    
#Solve height of a trapezoid
def trapezoid_height(base_short,base_long,area):
    return 2*(area/(base_short+base_long))

    
#Solve surface area of a trapezoid
def trapezoid_surface_are(base_short,base_long,height):
    return ((base_short+base_logn)/2)*height


#Solve a using pythagoras
def pythagoras_a(b,c):
    return math.sqrt((c**2)-(b**2))


#Solve b using pythagoras
def pythagoras_b(a,c):
    return math.sqrt((c**2)-(a**2))

    
#Solve c using pythagoras
def pythagoras_c(a,b):
    return math.sqrt((a**2)+(b**2))

    
def energy_evq(potential_difference,charge):
    return potential_difference*charge


def potential_dif_evq(energy,charge):
    return energy/charge


def charge_evq(energy,potential_difference):
    return energy/potential_difference

    
def power_piv(current, potential_difference):
    return current*potential_difference


def current_piv(power, potential_difference):
    return power/potential_difference

    
def potential_dif_piv(power, current):
    return power/current

    
def power_pet(energy,time): #0.0.9
    return energy/time


def energy_pet(power,time):
    return power*time

def time_pet(power,energy):
    return energy/power

def sequence_nth(first_term,term_number,common_difference):
    return first_term+(common_difference*(term_number-1))

def sequence_first(nth,term_number,common_difference):
    return nth-(common_difference*(term_number-1))

def sequence_difference(nth,first_term,term_number):
    return (nth-first_term)/(term_number-1)

def sequence_termnum(nth,first_term,common_difference):
    return ((nth-first_term)/common_difference)+1

def orbitalspeed_vrt(radius,time):
    return (2*(math.pi)*radius)/time

def radius_vrt(orbitalspeed,time):
    return (orbitalspeed*time)/(2*math.pi)

def orbittime_vrt(orbitalspeed,radius):
    return (2*math.pi*radius)/orbitalspeed

def cosine_side_a(b,c,A_radians):
    return math.sqrt((b**2+c**2)-2*(b*c*math.cos(A_radians)))

def cosine_side_b(a,c,B_radians):
    return math.sqrt(a**2+c**2-2*a*c*math.cos(B_radians))

def cosine_side_c(a,b,C_radians):
    return math.sqrt(a**2+b**2-2*a*b*math.cos(C_radians))

def cosine_angle_A(a,b,c):
    return math.acos(((b**2+c**2)-a**2)/(2*b*c))

def cosine_angle_B(a,b,c):
    return math.acos(((a**2+c**2)-b**2)/(2*a*c))

def cosine_angle_C(a,b,c):
    return math.acos(((a**2+b**2)-c**2)/(2*a*b))



#FORCES:

#(f(g)=mg) finds force of gravity (f(g)=mg) using mass and grav constant
def force_grav(mass,g):
    return mass * g
#(f(g)=mg) find mass using force of grav and g
def force_g_mass(force_g,g):
    return force_g / g
#(f(g)=mg) find grav constant using force of g and mass
def force_g_constant(force_g,mass):
    return force_g / mass

#(F(f)=u*F(n)) - finds force of friction (F(f)) using normal force and friction coefficent
def friction_force(n_force,f_coeff):
    return n_force * f_coeff
#(F(f)=u*F(n)) finds normal force (F(n)) using F(f) and friction coefficient (u)
def friction_normal(f_force,f_coeff):
    return f_force / f_coeff
#(F(f)=u*F(n)) finds friction coefficient (u) using F(f) and F(n)
def friction_u(f_force,n_force):
    return f_force / n_force

#the following only work when friction is the ONLY force!
#(a=ug) find acceleration using fric. coefficient (u) and grav constant
def aug_a(f_coeff,g):
    return f_coeff * g
#(a=ug) find fric. coefficient (u) using acceleration and grav constant
def aug_u(a,g):
    return a / g
#(a=ug) find grav constant using u and a
def aug_g(a,f_coeff):
    return a / f_coeff

#(u=F(f)/F(n)) find u with F(f) and F(n)
def u_coefficient(f_force,n_force):
    return f_force / n_force
#(u=F(f)/F(n)) find F(f) with u and F(n)
def u_friction(u,n_force):
    return u * n_force
#(u=F(f)/F(n)) find F(n) with u and F(f)
def u_normal(u,f_force):
    return f_force / u



#MIRRORS
#d(o) = distance (object)
#d(i) = distance (image)
#h(o) = height (object)
#h(i) = height (image)
#m = magnification 

#(h(i) = h(o)) for plane mirrors
def plane_mirror_hi(h_o):
    return h_o
def plane_mirror_ho(h_i):
    return h_i
#(d(i) = d(o)) for plane mirrors
def plane_mirror_di(d_o):
    return d_o
def plane_mirror_do(d_i):
    return d_i

#(C=2f) find radius (C) with focal point (f) for concave and convex mirrors
def c2f_c(f):
    return 2 * f
#(C=2f) find focal point with C
def c2f_f(C):
    return C / 2

#(f=(di*do/di+do)) find focal point (f) with d(i) and d(o)
def focal_point(d_i,d_o):
    numerator = d_i * d_o
    denominator = d_i + d_o
    return numerator / denominator
#d(i)=(f*do/do-f) find d(i) with focal point and d(o)
def mirror_distance_i(f,d_o):
    numerator = f * d_o
    denominator = d_o - f
    return numerator / denominator
#d(o)=(f*di/di-f) find d(o) with focal point and d(i)
def mirror_distance_o(f,d_i):
    numerator = f * d_i
    denominator = d_i - f
    return numerator / denominator

#the following equations are variations of m=(hi/ho)=(-di/do)
#find m with h(i) and h(o)
def mirror_mag_h(h_i,h_o):
    return h_i / h_o
#find m with d(i) and d(o)
def mirror_mag_d(d_i,d_o):
    neg_di = (-1) * d_i
    return neg_di / d_o
#find h(i) with m and h(o)
def mirror_hi_m(m,h_o):
    return m * h_o
#find h(i) with d(i), d(o), and h(o)
def mirror_hi_hodido(d_i,d_o,h_o):
    neg_di = (-1) * d_i
    numerator = neg_di * h_o
    return numerator / d_o
#find h(o) with m and h(i)
def mirror_ho_m(h_i,m):
    return h_i / m
#find h(o) with d(i), d(o), h(i)
def mirror_ho_hodido(d_i,d_o,h_i):
    neg_di = (-1) * d_i
    numerator = h_i * d_o
    return numerator / neg_di


#PENDULUMS
#T = period
#L = length of string (of pendulum)
#g = grav constant (acceleration of grav)

#T = 2(pi)*sqrt(L/g)

#find T with L and g
def pendulum_T(L,g):
    2pi = 2 * pi
    LG = L / g
    sqroot = math.sqrt(LG)
    return 2pi * sqroot
#find L with T and g
def pendulum_L(T,g):
    2pi = 2 * pi
    T2pi = T / 2pi
    T2pi_sq = T2pi * T2pi
    return g * T2pi_sq
#find g with T and L
def pendulum_g(T,L):
    2pi = 2 * pi
    2pi_sq = 2pi * 2pi
    T_sq = T * T
    numerator = L * 2pi_sq
    return numerator / T_sq




def help():
    webbrowser.open_new_tab('https://tinosps.wixsite.com/tiquations')
    #General
    print('''
A python package containing useful equations for science and maths.
Created by Tinos Psomadakis\n
          ''')
    #Commands
    print("Angles are always measured in radians")
    print('''
Commands:

quadratic(a,b,c) - Find quadratic formula from an equation like 3x^2+6x+2 = 0 where a=3, b=6 and c=2.
distance_dst(speed,time) - Find distance using speed and time
speed_dst(distance,time) - Find speed using distance and time
time_dst(distance,speed) - Find time using distance and speed
force_fma(mass,acceleration) - Find force using mass and acceleration
mass_fma(force,acceleration) - Find mass using force and acceleration
acceleration_fma(force,mass) - Find acceleration using force and mass
weight_wmg(mass, gravitational_field_strength) - Find weight using mass and gravitational field strength
mass_wmg(weight, gravitational_field_strength) - Find mass using weight and gravitational field strength
gravity_wmg(weight, mass) - Find gravitational field strength using weight and mass
circle_area_rad(radius) - Find area of a circle using radius
circle_area_dia(diameter) - Find area of a circle using diameter
circle_diam_rad(radius) - Find diameter of a circle using radius
circle_diam_are(area) - Find diameter of a circle using area
circle_circum(radius) - Find circumference of a circle
acceleration_avt(delta_velocity,time) - Find acceleration using change in velocity and time
delta_velocity_avt(acceleration,time) - Find change in velocity using acceleration and time
time_avt(acceleration,delta_velocity) - Find time taken using change in velocity and acceleration
pressure_fpa(force, area) - Find pressure using force and area
force_fpa(pressure, area) - Find force using pressure and area
area_fpa(force, pressure) - Find area using force and pressure
cylinder_vol(radius,height) - Find volume of cylinder
cylinder_surface_are(radius,height) - Find surface area of cylinder
trapezoid_area(base_short,base_long,height) - Find area of trapezoid
trapezoid_height(base_short,base_long,area) - Find height of trapezoid
trapezoid_surface_are(base_short,base_long,height) - Find surface are of trapezoid
pythagoras_a(b,c) - Solve for a in equation a²+b²=c²
pythagoras_b(a,c) - Solve for b in equation a²+b²=c²
pythagoras_c(a,b) - Solve for c in equation a²+b²=c²
energy_evq(potential_difference,charge) - Find energy using potential difference and charge
potential_dif_evq(energy,charge) - Find potential difference using energy and charge
charge_evq(energy,potential_difference) - Find charge using energy and potential difference
power_piv(current, potential_difference) - Find power using current and potential difference
current_piv(power, potential_difference) - Find current using power and potential difference
potential_dif_piv(power, current) - Find potential difference using power and current
power_pet(energy,time) - Find power using energy and time
energy_pet(power,time) - Find energy using power and time
time_pet(power,energy) - Find time using power and energy
sequence_nth(first_term,term_number,common_difference) - Find nth term of sequence
sequence_first(nth,term_number,common_difference) - Find the first term of a sequence
sequence_difference(nth,first_term,term_number) - Find difference of a sequence
sequence_termnum(nth,first_term,common_difference) - Find term number of a sequence
orbitalspeed_vrt(radius,time) - Find orbital speed using radius and orbit time
radius_vrt(orbitalspeed,time) - Find radius using orbital speed and orbit time
orbittime_vrt(orbitalspeed,radius) - Find orbit time using orbital speed and radius
cosine_side_a(b,c,A_radians) - Find side a using cosine rule
cosine_side_b(a,c,B_radians) - Find side b using cosine rule
cosine_side_c(a,b,C_radians) - Find side c using cosine rule
cosine_angle_A(a,b,c) - Find angle A using cosine rule
cosine_angle_B(a,b,c) - Find angle B using cosine rule
cosine_angle_C(a,b,c) - Find angle C using cosine rule

Usage:
hello = tiquations.example_xyz(5,72)
testing = tiquations.quadratic(1,2,-3)

          ''')
    
    #Built-in variables
    print('''
Built-in varaibles:
earth_g - Earth's gravitational pull strength in m/s² = 9.807
moon_g - The moon's gravitational pull strength in m/s² = 1.62
mars_g - Mars' gravitational pull strength in m/s² = 3.711
jupiter_g - Jupiter's gravitational pull strength in m/s² = 24.79
neptune_g - Neptune's gravitational pull strength in m/s² = 11.15
mercury_g - Mercury's gravitational pull strength in m/s² = 3.7
saturn_g - Saturn's gravitational pull strength in m/s² = 10.44
uranus_g - Uranus' gravitational pull strength in m/s² = 8.87
venus_g - Venus' gravitational pull strength in m/s² = 8.87
pluto_g - Pluto's gravitational pull strength in m/s² = 0.62
pi - First 16 numbers of pi = 3.141592653589793
eulersnum - Euler's number = 2.7182818284590452353602874713527
eulersmasch - Euler's Mascheroni Constant = 0.577215664901532860606512
golden_ratio - The golden ration = 1.6180339887498948420
sun_to_earth - Distance from Sun to the Earth in km = 149597870 
sun_to_mars - Distance from Sun to Mars in km = 227940000 
sun_to_mercury - Distance from Sun to Mercury in km = 57900000 
sun_to_venus - Distance from Sun to Venus in km = 108200000 
sun_to_jupiter - Distance from Sun to Jupiter in km = 778300000 
sun_to_neptune - Distance from Sun to Neptune in km = 4497100000 
sun_to_saturn - Distance from Sun to Saturn in km = 1427000000 
sun_to_uranus - Distance from Sun to Uranus in km = 2871000000 
sun_to_pluto - Distance from Sun to Pluto in km = 5913000000 
I_naught - I naught, for Mirror Equations = 0.000000000001
speed_of_light - Speed of Light in m/s² = 299792458
avogadros_num - Avogadro's Number = 602214086000000000000000
earth_mass - Mass of the Earth in kg = 5980000000000000000000000

Usage:
var = tiquations.example(pi,67)
weight = tiquations.weight_wmg(52, earth_g)

Type tiquations.variables() to see a full list with attached values
        ''')
