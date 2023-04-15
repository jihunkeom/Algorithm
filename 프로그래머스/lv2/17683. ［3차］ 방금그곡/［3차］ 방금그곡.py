def convert_mapping(data):
    sharp = {
        "C#": "c",
        "D#": "d",
        "F#": "f",
        "G#": "g",
        "A#": "a",
        "E#": "e",
    }
    tmp = []
    for x in data:
        if x == "#":
            chord = tmp.pop()
            tmp.append(sharp[chord + "#"])
        else:
            tmp.append(x)
    return "".join(tmp)

def solution(m, musicinfos):
    answer = []
    m = convert_mapping(m)
    
    for i in range(len(musicinfos)):
        music = musicinfos[i]
        music = music.split(",")
        start_time, end_time, title, chord = music
        start_time, end_time = start_time.split(":"), end_time.split(":")
        start_time = 60*int(start_time[0])+int(start_time[1])
        end_time = 60*int(end_time[0])+int(end_time[1])
        play_time = end_time-start_time
        if play_time <= 0:
            continue
        
        chord_list = convert_mapping(chord)
        if len(chord_list) > play_time:
            chord_list = chord_list[:play_time]
        else:
            repeat = play_time//len(chord_list)
            chord_list = chord_list * repeat
            chord_list += chord_list[:play_time-len(chord_list)]

        if m in chord_list:
            answer.append((play_time, i, title))
        
    if len(answer) > 0:
        answer = sorted(answer, key=lambda x: (-x[0], x[1]))
        return answer[0][-1]
    else:
        return "(None)"
    