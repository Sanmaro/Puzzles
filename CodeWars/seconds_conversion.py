# def format_duration(seconds):
#     if seconds == 0:
#         return "now"
#     human_friendly = []
#     conversion = {
#         "year": 31540000,
#         "day": 86400,
#         "hour": 3600,
#         "minute": 60
#     }
#     if seconds >= conversion["year"]:
#         years = seconds // conversion["year"]
#         human_friendly.append(f"{years} year" 
#             if years == 1 else f"{years} years")
#         seconds = seconds % conversion["year"]
#     if seconds >= conversion["day"]:
#         days = seconds // conversion["day"]
#         human_friendly.append(f"{days} day" 
#             if days == 1 else f"{days} days")
#         seconds = seconds % conversion["day"]
#     if seconds >= conversion["hour"]:
#         hours = seconds // conversion["hour"]
#         human_friendly.append(f"{hours} hour" 
#             if hours == 1 else f"{hours} hours")
#         seconds = seconds % conversion["hour"]
#     if seconds >= conversion["minute"]:
#         minutes = seconds // conversion["minute"]
#         human_friendly.append(f"{minutes} minute" 
#             if minutes == 1 else f"{minutes} minutes")
#         seconds = seconds % conversion["minute"]
#     if seconds > 0:
#         human_friendly.append(f"{seconds} second" 
#             if seconds == 1 else f"{seconds} seconds")
    
#     return (f"{", ".join(human_friendly[:-1])} and {human_friendly[-1]}"
#             if len(human_friendly) > 1 else human_friendly[-1]) 


def format_duration(seconds):
    if seconds == 0:
        return "now"
    conversion = {
        "year": 31536000,
        "day": 86400,
        "hour": 3600,
        "minute": 60
    }
    years = (seconds 
             // conversion["year"])
    days = ((seconds - (years * conversion["year"])) 
            // conversion["day"])
    hours = ((seconds 
             - (years * conversion["year"] + days * conversion["day"])) 
            // conversion["hour"])
    minutes = ((seconds 
             - (years * conversion["year"] + days * conversion["day"]
             + hours * conversion["hour"])) 
            // conversion["minute"])
    seconds = (seconds 
             - (years * conversion["year"] + days * conversion["day"]
             + hours * conversion["hour"] + minutes * conversion["minute"]))
    return None



print(format_duration(31536500))