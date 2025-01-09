from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.text import Text
import pylast
import time

API_KEY = "LastFM API KEY"
API_SECRET = "LastFM API SECRET"
USERNAME = "LastFM API USERNAME"
PASSWORD_HASH = pylast.md5("LastFM PASSWORD")

console = Console()

ascii_art = """
███████╗██╗░░░██╗██╗██╗░░░░░  ███████╗███╗░░░███╗
██╔════╝██║░░░██║██║██║░░░░░  ██╔════╝████╗░████║
█████╗░░╚██╗░██╔╝██║██║░░░░░  █████╗░░██╔████╔██║
██╔══╝░░░╚████╔╝░██║██║░░░░░  ██╔══╝░░██║╚██╔╝██║
███████╗░░╚██╔╝░░██║███████╗  ██║░░░░░██║░╚═╝░██║
╚══════╝░░░╚═╝░░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝░░░░░╚═╝

         Made by hrishavvv
"""

console.print(Text(ascii_art, style="bold cyan"))

def scrobble_artist_track(artist_name, track_name, times=1):
    try:
        console.print(Text("Authenticating with Last.fm...", style="bold magenta"))
        network = pylast.LastFMNetwork(
            api_key=API_KEY,
            api_secret=API_SECRET,
            username=USERNAME,
            password_hash=PASSWORD_HASH
        )
        console.print(Text("Authentication successful.", style="bold green"))

        with Progress(
            SpinnerColumn(style="bold cyan"),
            BarColumn(bar_width=None),
            TextColumn("{task.description}"),
            console=console,
            transient=True
        ) as progress:
            task = progress.add_task(f"Scrobbling [bold magenta]{artist_name} - {track_name}[/bold magenta]", total=times)

            for i in range(times):
                timestamp = int(time.time()) + i
                network.scrobble(artist=artist_name, title=track_name, timestamp=timestamp)
                time.sleep(1)
                progress.update(task, advance=1)

        console.print(Text(f"Successfully scrobbled {times} times: {artist_name} - {track_name}", style="bold green"))
    except Exception as e:
        console.print(Text(f"Error during scrobbling: {e}", style="bold red"))

artist = "Brakence"
track = "caffeine"

scrobble_artist_track(artist, track, times=1) 
