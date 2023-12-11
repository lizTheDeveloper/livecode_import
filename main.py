from manager_agent import prompt as manager_prompt
from producer_agent import prompt as producer_prompt

manager_response = manager_prompt("I'm producing a cool rap album about Python Data Structures. I need a set of lyrics for my rap album. Please make a plan for 5 tracks to give direction to the producer of lyrics. Please separate the track name and description on new lines so I can split the input by the new line character, and separate the track name from the track description with a : so I can split on the : character.")

for line in manager_response.split("\n"):
    split_line = line.split(":")
    print(split_line)
    track_description = split_line[1]
    track_name = split_line[0]
    producer_response = producer_prompt("You're producing a rap album, and the artist has defined several tracks they want. Please write the lyrics for a rap track on this topic: " + track_description)
    print(f"{track_name}: {producer_response}")