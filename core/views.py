from django.shortcuts import render

# Create your views here.

announcements = [
        {
            "id": 1,
            "title": "School Opening Moved to October 5",
            "content": (
                "The opening of classes has been moved from September 15 to October 5 due to weather conditions "
                "and safety measures. The adjustment is meant to ensure student safety and provide more preparation "
                "time for faculty and staff. Online platforms will remain active during the delay, allowing students "
                "to access preliminary learning materials. Parents and guardians are encouraged to regularly check "
                "the school’s official website for updates and further announcements."
            ),
        },
        {
            "id": 2,
            "title": "Midterm Exams Schedule Posted",
            "content": (
                "Midterm exams will be held from October 20 to October 25. The official exam schedule has been posted "
                "on the school bulletin board and uploaded to the student portal. Each department has organized review "
                "sessions to help students prepare. Students are reminded to bring their exam permits and valid IDs. "
                "Failure to present required documents may result in not being allowed to take the exam. For students "
                "who miss the exams, make-up exams will only be given to those with valid reasons and proper documentation."
            ),
        },
        {
            "id": 3,
            "title": "Campus Renovation Project",
            "content": (
                "The university is beginning a major campus renovation project that will last for the next 12 months. "
                "The project includes upgrades to classrooms, laboratories, and the student center. New study spaces will "
                "be created with modern designs to improve learning. The main library will also undergo expansion to "
                "provide more seating capacity and better digital resources. During construction, some pathways and buildings "
                "may be temporarily inaccessible. We ask for everyone's patience and cooperation throughout this process. "
                "Regular updates will be provided every month so students and staff remain informed about the progress."
            ),
        },
    ]

def home(request):
    return render(request, 'home.html', {'title': 'Home'})

def announcements_list(request):

    return render(request, 'announcement_list.html', {'announcements': announcements})

def announcements_detail(request, id):
    
    announcement = next((a for a in announcements if a["id"] == id), None)
    print("DEBUG announcement:", announcement)
    return render(request, 'announcement_detail.html', {'announcements': announcement})