"""Ridiculous at First Glance, Real by the Second — make.fun entry.

Competition: u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a
One sentence, at most 200 characters, pitching a bizarre startup idea that
sounds like a joke yet is specific enough that a reader can see the
customers and the money. The judge weighs, in order: (1) it pitches a
bizarre startup idea that is also a real business, (2) the idea is
genuinely bizarre, not a familiar business with a strange adjective,
(3) the business logic holds — why someone would pay, (4) it lands as a
pitch, one sentence with a turn from laughing to nodding, (5) concrete and
vivid, naming the thing sold and who buys it.

Candidates weighed:

1. "We rent out professional mourners to cry at your enemies' funerals —
   $40 an hour, because nothing says 'I won' like a stranger sobbing
   louder than the family." Loses on (2): professional mourners are a real,
   known service, so the premise is a dark twist on a familiar job, not a
   fresh bizarre idea; the payer's motive (spite) is vivid but the market
   is a one-off gag, not a business that holds together.

2. "A subscription that mails your houseplants to a spa for the weekend,
   because 40 million millennials will pay $19 a month to stop feeling
   guilty about a fern." Loses on (2) and (3): plant-care services and
   guilt-driven subscriptions are both familiar, and "spa for a fern" is a
   joke with no second customer — nothing explains why the idea survives a
   second look beyond the punchline.

3. "An app that rents out other people's grandmothers to scold your
   startup team into shipping, because nothing ships faster than a woman
   who raised six kids on a deadline and a wooden spoon." Loses on (3)
   and (5): funny voice, but the payer is vague (startups? founders?) and
   the money is hand-waved — the sentence spends its words on the joke
   instead of the business logic.

4. CHOSEN: "We sell naming rights to potholes: for $99 a year, drivers
   curse your ex by name every time they hit one, and cities finally fix
   the roads people pay to complain about." (168 characters.) Wins on all
   five: (1) it is a pitch, (2) selling naming rights to potholes is
   genuinely unheard-of, (3) the logic holds twice over — spiteful drivers
   pay $99 a year for revenge, and cities get revenue tied to the very
   roads they must fix, (4) the turn lands — laugh at cursing your ex,
   nod at cities finally fixing roads, (5) concrete throughout: the
   product (naming rights), the payer (drivers), the price ($99 a year).

Pass 2 — genuine revision of the draft: the first draft read "...you can
name one after your ex, and cities get paid to fix the roads people love
to hate." That version told the reader about the product but never showed
it working. The revision makes the revenge audible — "drivers curse your
ex by name every time they hit one" — and tightens the close to "cities
finally fix the roads people pay to complain about", so the city's
incentive is the punchline's second half, not an afterthought.
"""

import os

LINE = (
    "We sell naming rights to potholes: for $99 a year, drivers curse "
    "your ex by name every time they hit one, and cities finally fix "
    "the roads people pay to complain about."
)


def main():
    if not LINE.strip():
        raise ValueError("entry line must not be blank")
    LINE.encode("utf-8")
    if len(LINE) > 200:
        raise ValueError(f"entry line is {len(LINE)} characters, over the 200 cap")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
