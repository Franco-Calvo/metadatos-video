from pymediainfo import MediaInfo

video_file_path = "./video.mp4"

media_info = MediaInfo.parse(video_file_path)


def print_metadata(metadata, indent=0):
    for key, value in metadata.items():
        if isinstance(value, dict):
            print("  " * indent + str(key) + ":")
            print_metadata(value, indent + 1)
        else:
            print("  " * indent + f"{key}: {value}")


for track in media_info.to_data()["tracks"]:
    print(f"Track tipo: {track['track_type']}")
    print_metadata(track)
    print("-" * 40)
