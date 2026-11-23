#!/usr/bin/env python3
"""
Build The Vegas Cocks static site.

    python3 build.py   -> writes index.html, music.html, about.html, shop.html, contact.html

Edit the text here, rebuild, commit, push. GitHub Pages serves the result.
"""
import html
import os

# Contact form: Web3Forms access key (public by design). Leave "" until the key exists;
# the form then tells visitors the form is not switched on yet.
WEB3FORMS_KEY = "5cd63943-8ab8-4f3e-ad61-9cfc33a5001a"

BANDCAMP_ALBUM_URL = "https://thevegascocks.bandcamp.com/album/the-vegas-cocks"
BANDCAMP_EMBED = ("https://bandcamp.com/EmbeddedPlayer/album=2762444965/size=large/"
                  "bgcol=000000/linkcol=c9507f/tracklist=true/artwork=small/transparent=true/")
LANDR_URL = "https://artists.landr.com/vegascocks"
SHOP_URL = "https://the-vegas-cocks-shop.fourthwall.com"

STREAMING = [
    ("Spotify", "https://open.spotify.com/album/3jVNJiE29sZQa6CxbyOgcb"),
    ("Apple Music", "https://music.apple.com/us/album/1852807068"),
    ("YouTube Music", "https://music.youtube.com/playlist?list=OLAK5uy_niPRKUx9qKUjW5qp_Ye_uLIBnMB7eJHj4"),
    ("Amazon Music", "https://music.amazon.com/albums/B0G1V4DZZC"),
    ("Tidal", "http://www.tidal.com/album/473218780"),
    ("Deezer", "https://www.deezer.com/album/854554752"),
    ("Pandora", "https://www.pandora.com/artist/the-vegas-cocks/the-vegas-cocks/ALPb46w2fr5PdgP"),
    ("iHeartRadio", "https://www.iheart.com/artist/48607865/albums/360420062/"),
]

TRACKS = [
    ("Cocktail Queen", "2:44"), ("She Looks a Lot Like You", "2:19"), ("The Next Fool", "3:28"),
    ("Rainbow Toupe", "3:26"), ("Put It Away", "3:26"), ("Too Late", "3:45"),
    ("Three O'Clock Love", "4:24"), ("Empty Room", "3:02"), ("Easy To Fall", "3:43"),
]


def esc(s):
    return html.escape(s, quote=True)


NAV = [("index.html", "Home"), ("music.html", "Music"), ("about.html", "About"),
       ("shop.html", "Shop"), ("family.html", "Family"), ("contact.html", "Contact")]


def page(filename, title, description, body):
    items = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == filename else ""}>{l}</a></li>' for h, l in NAV)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=Barlow:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css?v=fam1">
</head>
<body>
<a class="skip" href="#content">Skip to content</a>
<header class="top">
  <a class="logo" href="index.html"><img src="img/the-vegas-cocks-1.png" alt="The Vegas Cocks" width="160" height="160"></a>
  <nav aria-label="Main"><ul>{items}</ul></nav>
</header>
<main id="content">
{body}
</main>
<footer class="foot">
  <p>&copy; The Vegas Cocks</p>
</footer>
<script src="js/site.js"></script>
</body>
</html>
"""


def player():
    return f"""
<iframe class="bc" title="The Vegas Cocks on Bandcamp" src="{BANDCAMP_EMBED}" seamless loading="lazy"
  style="border:0;width:100%;max-width:700px;height:470px"><a href="{BANDCAMP_ALBUM_URL}">The Vegas Cocks by The Vegas Cocks</a></iframe>
"""


def streaming_links():
    links = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{n}</a></li>' for n, u in STREAMING)
    return f'<ul class="stream">{links}</ul>'


def build_home():
    return f"""
<section class="hero">
  <img src="img/livej.jpg" alt="The Vegas Cocks live on stage" width="939" height="704">
  <div class="hero-text">
    <h1>Uncured high octane gutter-snipe rock and roll.</h1>
    <p>Our mission is to &hellip; Fuck it, we didn&rsquo;t have a mission. We just created sparkle blings from the blood and sweat and piss we exuded whilst trying to make a mockery of all the internalized suffering that was foisted upon us and given freely in large doses to intoxicating effect to unassuming and unsuspecting foul hain&rsquo;t all over everywhere. All are always welcome here.</p>
    <p><a class="btn" href="music.html">Listen now</a></p>
  </div>
</section>
<section class="band">
  <h2>Rock and roll for all the world&hellip;</h2>
  <p class="shout">Concocting an emotional dysphoria full of sound swelling shameful shoddy shit and joy and love and ashes and sand and bread</p>
  <p>and then the foot hit the cat and the cat jumped off the bed and the med was need and the pee was not green and the sage was wished for and the music is coming, oh yes, its coming down like all of raining hell fire of rc cola goodness shit it sure will as sure as the robins shake their thirst and the blue jays soar to heaven.</p>
</section>
<section class="listen">
  <h2>The Vegas Cocks</h2>
  {player()}
</section>
"""


def build_music():
    rows = "".join(f"<li><span>{esc(t)}</span><span>{d}</span></li>" for t, d in TRACKS)
    return f"""
<article class="prose">
  <h1>Music</h1>
  <p>The Vegas Cocks, 9 tracks. Name your price on Bandcamp, or stream it anywhere.</p>
  {player()}
  <h2>Tracks</h2>
  <ol class="tracks">{rows}</ol>
  <h2>Stream it</h2>
  {streaming_links()}
  <p class="small"><a href="{BANDCAMP_ALBUM_URL}" target="_blank" rel="noopener">Buy or download on Bandcamp</a> &middot; <a href="{LANDR_URL}" target="_blank" rel="noopener">All links on LANDR</a></p>
</article>
"""


def build_about():
    return f"""
<article class="prose">
  <h1>About</h1>
  <div class="two-col">
    <div>
      <p>The Vegas Cocks are a street-smart, mid-90s rock &amp; roll band out of Nashville, Tennessee, with the emphasis on rock.</p>
      <h2>Where the songs came from</h2>
      <ul>
        <li><strong>Too Late</strong> was a vinyl 45 mixed by Paul Mahern and released by Ramona Records of Indianapolis.</li>
        <li><strong>Three O&rsquo;Clock Love</strong> came out of a development deal with MCA Records and was produced by Brad Circone of the Toll.</li>
        <li><strong>Rainbow Toupe</strong> was produced by Joe Baldridge.</li>
      </ul>
      <p class="small">Tags: hard rock, rock, trash blues rock n&rsquo; roll, Nashville.</p>
    </div>
    <div class="side">
      <img src="img/cover.jpg" alt="The Vegas Cocks 45 sleeve: Too Late / Put It Away" width="2182" height="1676" loading="lazy">
      <img src="img/hatchposter.jpg" alt="Hatch Show Print poster: Hoo Doo Gurus with special guests The Vegas Cocks, Exit/In" width="537" height="720" loading="lazy">
      <img src="img/livevc.jpg" alt="The Vegas Cocks live" width="939" height="704" loading="lazy">
    </div>
  </div>
</article>
"""


def build_shop():
    if SHOP_URL:
        card = f"""<a class="product" href="{SHOP_URL}/products/the-vegas-cocks-logo-tee">
      <img src="img/vegascocks-tee-front.jpg" alt="The Vegas Cocks Logo Tee" loading="lazy">
      <span class="product-name">The Vegas Cocks Logo Tee</span>
      <span class="product-price">$30</span>
      <span class="product-note">Preview: the store link goes live at launch</span>
    </a>"""
    else:
        card = '<div class="ph" aria-hidden="true">T-shirt<br><small>coming soon</small></div>'
    return f"""
<article class="prose">
  <h1>Shop</h1>
  <p>Merch is on its way: shirts and other gear, printed and shipped on demand. Check back soon, or <a href="contact.html">send a note</a> and we&rsquo;ll tell you when it opens.</p>
  <div class="products">
    {card}
    <div class="ph" aria-hidden="true">Hoodie<br><small>coming soon</small></div>
    <div class="ph" aria-hidden="true">Stickers<br><small>coming soon</small></div>
  </div>
  <p><a class="btn" href="{BANDCAMP_ALBUM_URL}" target="_blank" rel="noopener">Get the album on Bandcamp</a></p>
</article>
"""


def build_contact():
    return f"""
<article class="prose">
  <h1>Contact</h1>
  <p>Booking, press, or just want to say something? Send a message.</p>
  <form id="contact-form" class="form" action="https://api.web3forms.com/submit" method="POST" data-key="{WEB3FORMS_KEY}">
    <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
    <input type="hidden" name="subject" value="New message from The Vegas Cocks website">
    <input type="hidden" name="from_name" value="The Vegas Cocks website">
    <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
    <label>Your name (required)<input name="name" required autocomplete="name"></label>
    <label>Your email (required)<input type="email" name="email" required autocomplete="email"></label>
    <label>Subject<input name="subject_line"></label>
    <label>Your message<textarea name="message" rows="6" required></textarea></label>
    <button class="btn" type="submit">Send</button>
    <p class="form-status" role="status" aria-live="polite"></p>
  </form>
</article>
"""


SITE_ID = "vegas-cocks"


def build_family():
    """Family page: cards for the other family sites, read from family.json."""
    import json
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "family.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    cards = []
    for f in data:
        if f["id"] == SITE_ID:
            continue
        pic = ('<a class="fam-pic" href="%s" rel="noopener"><img src="%s" alt="%s" loading="lazy" '
               'referrerpolicy="no-referrer" onerror="this.parentNode.remove()"></a>'
               % (esc(f["url"]), esc(f["image"]), esc(f["name"]))) if f.get("image") else ""
        cards.append('<article class="fam-card">%s<h3><a href="%s" rel="noopener">%s</a></h3><p>%s</p></article>'
                     % (pic, esc(f["url"]), esc(f["name"]), esc(f.get("blurb", ""))))
    return '''<article class="prose">
  <h1>Family</h1>
  <p class="lede">Artists, makers, poets, and saints.</p>
  <div class="fam-grid">%s</div>
</article>''' % "".join(cards)


PAGES = [
    ("index.html", "The Vegas Cocks – Uncured high octane gutter-snipe rock and roll",
     "The Vegas Cocks: street-smart, mid-90s rock & roll from Nashville, Tennessee. Listen to the album.", build_home),
    ("music.html", "Music – The Vegas Cocks", "Listen to The Vegas Cocks: 9 tracks on Bandcamp and every major streaming service.", build_music),
    ("about.html", "About – The Vegas Cocks", "About The Vegas Cocks, a street-smart mid-90s rock & roll band from Nashville, Tennessee.", build_about),
    ("shop.html", "Shop – The Vegas Cocks", "The Vegas Cocks merch: shirts and gear, coming soon.", build_shop),
    ("family.html", "Family – The Vegas Cocks", "The artists and makers in The Vegas Cocks family of websites.", build_family),
    ("contact.html", "Contact – The Vegas Cocks", "Contact The Vegas Cocks for booking and press.", build_contact),
]

if __name__ == "__main__":
    for fname, title, desc, fn in PAGES:
        with open(fname, "w", encoding="utf-8") as f:
            f.write(page(fname, title, desc, fn()))
        print("wrote", fname)
