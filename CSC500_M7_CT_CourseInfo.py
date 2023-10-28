room_numbers = {'CSC101': 3004, 'CSC102': 4501, 'CSC103': 6755,
                'NET110': 1244, 'COM241': 1411}
instructors = {'CSC101': 'Haynes', 'CSC102': 'Alvarado', 'CSC103': 'Rich',
               'NET110': 'Burke', 'COM241': 'Lee'}
meeting_time = {'CSC101': '8:00 a.m.', 'CSC102': '9:00 a.m.',
                'CSC103': '10:00 a.m.', 'NET110': '11:00 a.m.',
                'COM241': '1:00 p.m.'}

print('\nCourse information: room, instructor, time.')

done = False
while done is False:
    course = input("\nEnter a course number ('q' to quit): ")
    if course == 'q':
        done = True
    elif course in room_numbers:
        print('\n  {} COURSE INFO'.format(course))
        print('    Room Number: {}'.format(room_numbers[course]))
        print('    Instructor: {}'.format(instructors[course]))
        print('    Meeting Time: {}'.format(meeting_time[course]))
    else:
        print('Invalid course number.')
