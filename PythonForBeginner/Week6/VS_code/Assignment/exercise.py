import requests


def main():
    search_term = input("Please enter a search term: ")

    # Perform a search using iTunes Search Service
    url = f"https://itunes.apple.com/search?term={search_term}&entity=album"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        result_count = data["resultCount"]

        print(f"The search returned {result_count} results.")

        for result in data["results"]:
            artist_name = result["artistName"]
            album_name = result["collectionName"]
            track_count = result["trackCount"]

            print(
                f"Artist: {artist_name} - Album: {album_name} - Track Count: {track_count}")
    else:
        print("An error occurred while fetching data from iTunes.")


if __name__ == "__main__":
    main()
