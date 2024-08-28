from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sistec(request):
   s = '''
   <img></img>
   <h1 align="center" style="color:blue">Sagar Group of Institution</h1>
   <p>Sagar Group of Institutions which was established in the year 2007 under the aegis of Shri Agrawal Educational & Welfare Society with the main objective of imparting quality education.

Sagar Group of Institutions have emerged as a group of Best Private Colleges in Bhopal with its state-of-the-art facility and its expertise in Engineering, Pharmacy, and MBA education. Three institutional campuses rich in infrastructure and amenities proudly flourish under the aegis of the brand Sagar Group of Institutions.

The brand has a strong motivation towards innovation in curriculum implementation with its unique industry-oriented pedagogy. It further aspires to be a part of an educational revolution in technical education, impacting advanced futuristic technologies in the national and international framework, and aims to be one of the finest providers of technical education in India.

</p>
<h1 align="center" style="color:red">Engineering</h1>
<p>The B.Tech. Engineering Program at Sagar Group of Institutions is developed from an industrial point of view, with a great focus on modern technologies employed in the industries. Engineers are the focal point in our economy to design, test, and develop the next generation of products and services for the betterment of society. In this regard, the pedagogy is designed based on industry-oriented training modules a level extra than the standard university curriculum. Similarly, the MTech Engineering Program is developed from a research point of view to inculcate the spirit of innovation and development in Science & Technology.</p>

<h1 style="color:brown">B.Tech</h1>
<ul>
<li>Civil Engineering</li>
<li>Computer Science & Engineering</li>
<li>Computer Science & Information Technology</li>
<li>CSE with Artificial Intelligence and Data Science</li>
<li>CSE with Artificial Intelligence and Machine Learning</li>
<li>CSE with Internet of Things</li>
<li>CSE with Cyber Security</li>
<li>Electrical & Electronics Engineering</li>
<li>Electrical Engineering</li>
<li>Electronics & Communication Engineering</li>
<li>Mechanical Engineering</li>
</ul>

<h1 style="color:maroon">M.Tech</h1>
<ul>
<li>Computer Science & Engineering</li>
<li>Construction Technology and Management</li>
<li>Digital Communication</li>
<li>Machine Design</li>
<li>Power System</li>
<li>Structural Engineering</li>
<li>Thermal Power & Engineering</li>
<li>Very Large Scale Integration (VLSI) Design</li>
</ul>
   '''
   return HttpResponse(s)

