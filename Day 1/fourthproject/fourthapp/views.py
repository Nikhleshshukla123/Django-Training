from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
   s = '''
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


def about(request):
    a = '''
        <p>Sagar Group believes in its value system and is constantly working towards its mission of ‘building nation.’ It has established itself from one of the largest business conglomerates to a sizable corporate business house in central India. The group caters to the basic needs of individuals and largely impacts communities in healthcare, industry (textile & food processing), education, and real estate sectors impacting five lakh lives daily.

It came into existence in 1983, under the visionary leadership of its founder and chairman Mr. Sudhir Kumar Agrawal realizing the vision of contributing to the basic needs of individuals. Since its journey of over four decades, it’s committed to its customers to excel for a good life and is an integral part of the success story of Madhya Pradesh, India. The group contributes to the GDP of India having its footprint of exports to 20+ countries. It is supporting the farmers of the state by taking their produce to the world. The group offers career options to 6000+ professionals of different skill set with 60% diversity ratio empowering women with employment.

Its venture in healthcare is bringing smiles back into the lives of people and has emerged as the best hospital in Bhopal and is working towards a healthy Madhya Pradesh and Ayushman Bharat. Its network of 25000+ students with 2000+ highly skilled faculties is nurturing and empowering the youth with education and is igniting their minds for a better tomorrow. The group has been developing partners to drive a positive impact on communities with a focus on energy, nature, waste, and people towards sustainable development. In its journey of regeneration and sustainability, it is reducing its carbon footprint equivalent to the plantation of 4 lakh trees, providing free education with mid-day meals to 1500+ students.</p>

 <h1 align="center" style="color:blue">Sagar Group Ventures</h1>

 <h1 align="center" style="color:blue">Sagar Manufacturers</h1>
 <p>Sagar Manufacturers Pvt. Ltd. (SMPL) is the industrial wing of Sagar Group, a spinning mill with all the latest technologies and machinery. SMPL has pledged to use the best of fibers to produce superior quality yarns — “Sagar Yarn”. The company has a footprint in over 20+ countries where the exports have expanded. The industrial unit of Sagar Manufacturers Private Limited is a fully automated industrial unit having the ideal combination of machinery set up from leading brands of the world like Truetzschler, Reiter, Luwa, and Electrojet KTTM. SMPL has been accorded with the status of "STAR EXPORT HOUSE" by the Ministry of Commerce and Industry, Government of India, and the cotton yarn manufacturing company is ISO 9001:2015 certified.</p>

  <h1 align="center" style="color:blue">Sagar Nutriments</h1>
  <p>The food processing venture of Sagar Group is Central India's fully automated most advanced rice milling unit. SNPL is a vertically integrated rice milling unit offering a wide range of basmati & non-basmati rice. It works very closely with its customers spreading the fragrance and taste of Paddy grown in fields of Madhya Pradesh From every atom to each ton, Joy in Every Grain.</p>

   <h1 align="center" style="color:blue">Sagar Public School</h1>
   <p>Sagar Public School (SPS Bhopal) imparts world-class schooling through the chain of public schools affiliated to the Central Board of Secondary Education (CBSE) with campuses at Saket Nagar, Gandhi Nagar, Rohit Nagar, Ratibad, Katara Extension, and Dwarka Dham. SPS Bhopal started off its journey in 2001 and in the last 23 years, SPS has grown by leaps and bounds to take its place among the top schools of central India. With an enrolment of 11000 active students, SPS Bhopal also enjoys the distinction of being one of the largest group of schools in Central India. Today, Sagar Public Schools are considered the most preferred brand for holistic education, and with the Indian value system at its core, it features amongst the top 100 schools in India.</p>

   <h1 align="center" style="color:blue">SISTec</h1>
   <p>Sagar Colleges “SISTec” are a group of techno-skilled educational institutes in Bhopal committed to providing industry-oriented education in the field of engineering, pharmacy, and management with its unique pedagogy and focus on hands-on training. Sagar Colleges are known for imparting skill-based education making them rank among the best engineering colleges in Bhopal, with the ultimate aim of campus to corporate providing genuine placements to its students. With its state-of-the-art lush green campuses at Gandhi Nagar and Ratibad, Sagar Colleges are the most preferred and popular destination for budding technocrats. Three engineering colleges [Sagar Institute of Science and Technology (SISTec), Sagar Institute of Science Technology and Research (SISTec-R) and Sagar Institute of Science Technology and Engineering (SISTec-E)], a pharmacy institute [Sagar Institute of Pharmacy and Technology (SIPTec)], and a management school [Sagar Institute of Science and Technology – School of Management Studies (SISTec MBA)] proudly flourish under the aegis of Sagar Group of Institutions.</p>

    <h1 align="center" style="color:blue">Agrawal Builders</h1>
    <p>The construction, real-estate and infrastructure development arm of Sagar Group started way back in 1983 from a single-room company. It has expanded exponentially to be the real estate giant of Central India. It has brought smiles to the faces of 10000+ happy families to emerge as the most trusted Real Estate Brand in Housing Sector. The vertically integrated and innovation-focused company uses modern technologies in construction and has successfully executed ~ 95% of projects before time to deliver over 22+ projects before time with green and sustainable infrastructure.</p>

    <h1 align="center" style="color:blue">Abhay Sagar Foundation</h1>
    <p>Abhay Sagar Foundation is the community service arm of Sagar Group. The foundation was established in 2014. It is with a mission to bring smiles and social upliftment to the lives of people contributing towards the upliftment of under-privileged sections of society. It is working closely in the areas of education, healthcare, social development and environment sustainability to strengthen the communities.</p>
    '''
    return HttpResponse(a)

def contact(request):
    c = '''
        <h1>Contact Us</h1>
        <h1>SISTec Gandhi Nagar</h1>
        <p>SISTec Gandhi Nagar Campus flourishing under the aegis of Sagar Group of Institutions® lies within the heart of the city, Gandhi Nagar, Bhopal. The engineering, pharmacy, and MBA college campus is well connected and easily reachable by all modes of transportation. The college is located just opposite the Raja Bhoj International Airport (2.5 km away) which can easily be covered on foot. It is 17 km away from the Inter-State Bus Terminal (ISBT) located at Rani Kamplapati which is a mere half-hour ride. The nearest railway stations are Bhopal Junction (12 km away) and Rani Kamplapati (18 km away). Public transport is easily available through all corners of the city and popular cab services like Ola and Uber can also be availed.

</p>

<h1>Address</h1>
<ul>
<li>SISTec Gandhi Nagar Campus</li>
<li>Opposite International Airport, Bhopal (M.P.) 462036</li>
</ul>

<h1>Contact Details</h1>
<ul>
<li>Reception
-
9977995985</li>
<li>Admissions
-
admissions@sistec.ac.in</li>
<li>Placements
-
grouphead.crm@sistec.ac.in</li>
<li>Admission & Placement
-
9109975760</li>
</ul>

'''
    return HttpResponse(c)