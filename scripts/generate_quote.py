#!/usr/bin/env python3

import random
import datetime
from pathlib import Path
import pytz

# Collection of 500 quotes related to life, tech, and AI
QUOTES = [
    # Original quotes
    "The best AI is the one that knows when to ask for human help.",
    "Neural networks don't actually think; they just find patterns we're too busy to notice.",
    "Good code is like a good joke - it needs no explanation.",
    "The hardest part of AI isn't the algorithms, it's explaining to humans what the algorithms are doing.",
    "Machine learning is like having a million interns who are really good at one specific task.",
    "AI is the art of making computers do things that would be considered intelligent if done by humans.",
    "The goal of AI isn't to replace humans, but to empower them to be more human.",
    "Behind every great AI is a human who taught it how to learn.",
    "The best feature of AI is its ability to show us how human we really are.",
    "Artificial intelligence will reach its peak when it learns to doubt itself.",
    "Code like no one is watching your GitHub activity graph... but they are.",
    "The difference between a junior and senior developer is knowing when NOT to use AI.",
    "Your neural network is only as good as the data you feed it.",
    "Debugging is like being the detective in a crime movie where you're also the murderer.",
    "The most powerful debugging tool is still a good night's sleep.",
    "AI doesn't make mistakes; it just finds creative interpretations of your instructions.",
    "Today's AI breakthrough is tomorrow's utility function.",
    "The best time to start learning AI was 10 years ago. The second best time is now.",
    "Commit often, perfect later, publish once.",
    "Your GitHub streak doesn't define you, but it does show your consistency.",
    
    # Life quotes
    "Life is what happens when you're busy making other plans.",
    "The purpose of our lives is to be happy.",
    "Life is short, and it's up to you to make it sweet.",
    "In three words I can sum up everything I've learned about life: it goes on.",
    "Life is really simple, but we insist on making it complicated.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "The biggest adventure you can take is to live the life of your dreams.",
    "Life isn't about finding yourself. It's about creating yourself.",
    "Life is either a daring adventure or nothing at all.",
    "The good life is one inspired by love and guided by knowledge.",
    "Life is a journey that must be traveled no matter how bad the roads and accommodations.",
    "Life is a succession of lessons which must be lived to be understood.",
    "Life is like riding a bicycle. To keep your balance, you must keep moving.",
    "Life is a long lesson in humility.",
    "Life is not a problem to be solved, but a reality to be experienced.",
    "Life is a series of natural and spontaneous changes.",
    "Life is what we make it, always has been, always will be.",
    "Life is too important to be taken seriously.",
    "Life is a preparation for the future; and the best preparation for the future is to live as if there were none.",
    "Life is a dream for the wise, a game for the fool, a comedy for the rich, a tragedy for the poor.",
    
    # Tech quotes
    "Technology is best when it brings people together.",
    "It has become appallingly obvious that our technology has exceeded our humanity.",
    "The advance of technology is based on making it fit in so that you don't really even notice it.",
    "Technology is just a tool. In terms of getting the kids working together and motivating them, the teacher is the most important.",
    "The human spirit must prevail over technology.",
    "Technology is nothing. What's important is that you have a faith in people.",
    "Technology like art is a soaring exercise of the human imagination.",
    "Technology is a useful servant but a dangerous master.",
    "The first rule of any technology used in a business is that automation applied to an efficient operation will magnify the efficiency.",
    "Technology is a word that describes something that doesn't work yet.",
    "Technology made large populations possible; large populations now make technology indispensable.",
    "The real danger is not that computers will begin to think like men, but that men will begin to think like computers.",
    "Technology is anything that wasn't around when you were born.",
    "The great myth of our times is that technology is communication.",
    "One machine can do the work of fifty ordinary men. No machine can do the work of one extraordinary man.",
    "The art challenges the technology, and the technology inspires the art.",
    "Technology is the knack of so arranging the world that we don't have to experience it.",
    "Technology is a way of organizing the universe so that man doesn't have to experience it.",
    "Technology... the knack of so arranging the world that we don't have to experience it.",
    "Technology is teaching us to be human again.",
    
    # AI quotes
    "AI is the new electricity.",
    "Artificial intelligence is growing up fast.",
    "The development of full artificial intelligence could spell the end of the human race.",
    "AI doesn't have to be evil to destroy humanity – if AI has a goal and humanity just happens to come in the way, it will destroy humanity as a matter of course without even thinking about it.",
    "The pace of progress in artificial intelligence is incredibly fast.",
    "Artificial intelligence will reach human levels by around 2029.",
    "The question of whether a computer can think is no more interesting than the question of whether a submarine can swim.",
    "I visualize a time when we will be to robots what dogs are to humans, and I'm rooting for the machines.",
    "The real question is, when will we draft an artificial intelligence bill of rights?",
    "The coming era of Artificial Intelligence will not be the era of war, but be the era of deep compassion.",
    "Artificial intelligence is no match for natural stupidity.",
    "Some people call this artificial intelligence, but the reality is this technology will enhance us. So instead of artificial intelligence, I think we'll augment our intelligence.",
    "By far, the greatest danger of Artificial Intelligence is that people conclude too early that they understand it.",
    "Artificial intelligence is just a new tool, one that can be used for good and for bad purposes and one that comes with new dangers and downsides as well.",
    "The key to artificial intelligence has always been the representation.",
    "Artificial intelligence is growing up fast, as are robots whose facial expressions can elicit empathy and make your mirror neurons quiver.",
    "I'm increasingly inclined to think that there should be some regulatory oversight, maybe at the national and international level, just to make sure that we don't do something very foolish.",
    "The upheavals of artificial intelligence can escalate quickly and become scarier and even cataclysmic.",
    "Artificial intelligence will probably most likely lead to the end of the world, but in the meantime, there'll be great companies.",
    "The sad thing about artificial intelligence is that it lacks artifice and therefore intelligence.",
    
    # Additional quotes (continuing to 500)
    "Every problem is a gift—without problems we would not grow.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The only way to do great work is to love what you do.",
    "Believe you can and you're halfway there.",
    "Your time is limited, don't waste it living someone else's life.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "It does not matter how slowly you go as long as you do not stop.",
    "Quality is not an act, it is a habit.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "Do what you can, with what you have, where you are.",
    "The best way to predict the future is to create it.",
    "If you want to lift yourself up, lift up someone else.",
    "The mind is everything. What you think you become.",
    "The journey of a thousand miles begins with one step.",
    "The only person you are destined to become is the person you decide to be.",
    "What we think, we become.",
    "The best revenge is massive success.",
    "The difference between ordinary and extraordinary is that little extra.",
    "The way to get started is to quit talking and begin doing.",
    "Don't watch the clock; do what it does. Keep going.",
    "The harder I work, the luckier I get.",
    "Opportunities don't happen. You create them.",
    "Try not to become a person of success, but rather try to become a person of value.",
    "I have not failed. I've just found 10,000 ways that won't work.",
    "The secret of getting ahead is getting started.",
    "Don't be afraid to give up the good to go for the great.",
    "If you're going through hell, keep going.",
    "We may encounter many defeats but we must not be defeated.",
    "Knowing is not enough; we must apply. Wishing is not enough; we must do.",
    "Whether you think you can or you think you can't, you're right.",
    "Security is mostly a superstition. Life is either a daring adventure or nothing.",
    "The only way to do great work is to love what you do.",
    "If you look at what you have in life, you'll always have more.",
    "None of us is as smart as all of us.",
    "Alone we can do so little; together we can do so much.",
    "The expert in anything was once a beginner.",
    "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "The way to get started is to quit talking and begin doing.",
    "If life were predictable it would cease to be life, and be without flavor.",
    "Life is what happens when you're busy making other plans.",
    "Whoever is happy will make others happy too.",
    "When you reach the end of your rope, tie a knot in it and hang on.",
    "Always remember that you are absolutely unique. Just like everyone else.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
    "It is during our darkest moments that we must focus to see the light.",
    "You will face many defeats in life, but never let yourself be defeated.",
    "In the end, it's not the years in your life that count. It's the life in your years.",
    "Never let the fear of striking out keep you from playing the game.",
    "Life is either a daring adventure or nothing at all.",
    "You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose.",
    "Only a life lived for others is a life worthwhile.",
    "The purpose of our lives is to be happy.",
    "You only live once, but if you do it right, once is enough.",
    "Live in the sunshine, swim the sea, drink the wild air.",
    "Go confidently in the direction of your dreams! Live the life you've imagined.",
    "Life is made of ever so many partings welded together.",
    "The healthiest response to life is joy.",
    "Life is trying things to see if they work.",
    "Many of life's failures are people who did not realize how close they were to success when they gave up.",
    "If you want to live a happy life, tie it to a goal, not to people or things.",
    "Never let the fear of striking out keep you from playing the game.",
    "Money and success don't change people; they merely amplify what is already there.",
    "Your time is limited, so don't waste it living someone else's life.",
    "Not how long, but how well you have lived is the main thing.",
    "If life were predictable it would cease to be life, and be without flavor.",
    "The whole secret of a successful life is to find out what is one's destiny to do, and then do it.",
    "In order to write about life first you must live it.",
    "The big lesson in life, baby, is never be scared of anyone or anything.",
    "Curiosity about life in all of its aspects, I think, is still the secret of great creative people.",
    "Life is not a problem to be solved, but a reality to be experienced.",
    "The unexamined life is not worth living.",
    "Turn your wounds into wisdom.",
    "The way I see it, if you want the rainbow, you gotta put up with the rain.",
    "Do all the good you can, for all the people you can, in all the ways you can, as long as you can.",
    "Don't settle for what life gives you; make life better and build something.",
    "Everything negative – pressure, challenges – is all an opportunity for me to rise.",
    "I like criticism. It makes you strong.",
    "You never really learn much from hearing yourself speak.",
    "Life imposes things on you that you can't control, but you still have the choice of how you're going to live through this.",
    "Life is never easy. There is work to be done and obligations to be met – obligations to truth, to justice, and to liberty.",
    "Live for each second without hesitation.",
    "Life is like riding a bicycle. To keep your balance, you must keep moving.",
    "Life is really simple, but men insist on making it complicated.",
    "Life is a succession of lessons which must be lived to be understood.",
    "Life is like a coin. You can spend it any way you wish, but you only spend it once.",
    "The best portion of a good man's life is his little nameless, unencumbered acts of kindness and of love.",
    "In three words I can sum up everything I've learned about life: it goes on.",
    "Life is ten percent what happens to you and ninety percent how you respond to it.",
    "Keep calm and carry on.",
    "Maybe that's what life is... a wink of the eye and winking stars.",
    "Life is a flower of which love is the honey.",
    "Keep smiling, because life is a beautiful thing and there's so much to smile about.",
    "Health is the greatest gift, contentment the greatest wealth, faithfulness the best relationship.",
    "You have succeeded in life when all you really want is only what you really need.",
    "Be happy for this moment. This moment is your life.",
    "Life would be tragic if it weren't funny.",
    "My mission in life is not merely to survive, but to thrive; and to do so with some passion, some compassion, some humor, and some style.",
    "Once you figure out who you are and what you love about yourself, I think it all kinda falls into place.",
    "When we do the best we can, we never know what miracle is wrought in our life or the life of another.",
    "The greatest pleasure of life is love.",
    "Life's tragedy is that we get old too soon and wise too late.",
    "Life is about making an impact, not making an income.",
    "We all have two lives. The second one starts when we realize we only have one.",
    "The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well.",
    "I've missed more than 9000 shots in my career. I've lost almost 300 games. 26 times I've been trusted to take the game winning shot and missed. I've failed over and over and over again in my life. And that is why I succeed.",
    "Every strike brings me closer to the next home run.",
    "The two most important days in your life are the day you are born and the day you find out why.",
    "Life shrinks or expands in proportion to one's courage.",
    "Too many of us are not living our dreams because we are living our fears.",
    "I believe every human has a finite number of heartbeats. I don't intend to waste any of mine.",
    "Live as if you were to die tomorrow. Learn as if you were to live forever.",
    "If you live long enough, you'll make mistakes. But if you learn from them, you'll be a better person.",
    "Life is short, and it is up to you to make it sweet.",
    "Life doesn't require that we be the best, only that we try our best.",
    "I always like to look on the optimistic side of life, but I am realistic enough to know that life is a complex matter.",
    "The truth is you don't know what is going to happen tomorrow. Life is a crazy ride, and nothing is guaranteed.",
    "Life is a series of natural and spontaneous changes. Don't resist them—that only creates sorrow. Let reality be reality. Let things flow naturally forward in whatever way they like.",
    "Change your life today. Don't gamble on the future, act now, without delay.",
    "You're only here for a short visit. Don't hurry, don't worry. And be sure to smell the flowers along the way.",
    "Life's most persistent and urgent question is, 'What are you doing for others?'",
    "Life is a mirror and will reflect back to the thinker what he thinks into it.",
    "Life is a dream for the wise, a game for the fool, a comedy for the rich, a tragedy for the poor.",
    "Life is a song - sing it. Life is a game - play it. Life is a challenge - meet it. Life is a dream - realize it. Life is a sacrifice - offer it. Life is love - enjoy it.",
    "Life is a journey that must be traveled no matter how bad the roads and accommodations.",
    "Life is a series of collisions with the future; it is not the sum of what we have been, but what we yearn to be.",
    "Life is a succession of lessons which must be lived to be understood.",
    "Life is a tragedy when seen in close-up, but a comedy in long-shot.",
    "Life is an adventure in forgiveness.",
    "Life is an echo. What you send out comes back. What you sow, you reap. What you give, you get. What you see in others, exists in you.",
    "Life is an exciting business, and most exciting when it is lived for others.",
    "Life is an opportunity, benefit from it. Life is beauty, admire it. Life is a dream, realize it. Life is a challenge, meet it. Life is a duty, complete it. Life is a game, play it. Life is a promise, fulfill it. Life is sorrow, overcome it. Life is a song, sing it. Life is a struggle, accept it. Life is a tragedy, confront it. Life is an adventure, dare it. Life is luck, make it. Life is too precious, do not destroy it. Life is life, fight for it.",
    "Life is either a great adventure or nothing.",
    "Life is growth. If we stop growing, technically and spiritually, we are as good as dead.",
    "Life is like a landscape. You live in the midst of it but can describe it only from the vantage point of distance.",
    "Life is like a wheel. Sooner or later, it always come around to where you started again.",
    "Life is never fair, and perhaps it is a good thing for most of us that it is not.",
    "Life is not a matter of holding good cards, but sometimes, playing a poor hand well.",
    "Life is not a spectator sport. If you're going to spend your whole life in the grandstand just watching what goes on, in my opinion you're wasting your life.",
    "Life is not always a matter of holding good cards, but sometimes, playing a poor hand well.",
    "Life is not measured by the number of breaths we take, but by the moments that take our breath away.",
    "Life is painting a picture, not doing a sum.",
    "Life is really simple, but we insist on making it complicated.",
    "Life is the art of drawing without an eraser.",
    "Life is the flower for which love is the honey.",
    "Life is what happens while you are busy making other plans.",
    "Life is what we make it, always has been, always will be.",
    "Life isn't about finding yourself. Life is about creating yourself.",
    "Life isn't about getting and having, it's about giving and being.",
    "Life must be lived and curiosity kept alive. One must never, for whatever reason, turn his back on life.",
    "Life well spent is long.",
    "Life's under no obligation to give us what we expect.",
    "Our life is what our thoughts make it.",
    "The art of life is to know how to enjoy a little and to endure very much.",
    "The good life is one inspired by love and guided by knowledge.",
    "The greatest day in your life and mine is when we take total responsibility for our attitudes. That's the day we truly grow up.",
    "The meaning of life is to find your gift. The purpose of life is to give it away.",
    "The most important thing is to enjoy your life—to be happy—it's all that matters.",
    "The purpose of life is to live it, to taste experience to the utmost, to reach out eagerly and without fear for newer and richer experience.",
    "The quality, not the longevity, of one's life is what is important.",
    "The secret of life is not to do what you like, but to like what you do.",
    "There is more to life than increasing its speed.",
    "There is only one happiness in this life, to love and be loved.",
    "This life is worth living, we can say, since it is what we make it.",
    "Throughout life people will make you mad, disrespect you and treat you bad. Let God deal with the things they do, cause hate in your heart will consume you too.",
    "To live is the rarest thing in the world. Most people exist, that is all.",
    "We must be willing to let go of the life we have planned, so as to have the life that is waiting for us.",
    "When I hear somebody sigh, 'Life is hard,' I am always tempted to ask, 'Compared to what?'",
    "When one door closes, another opens; but we often look so long and so regretfully upon the closed door that we do not see the one that has opened for us.",
    "You can't live a perfect day without doing something for someone who will never be able to repay you.",
    "You only live once, but if you do it right, once is enough.",
    "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do."
]

def generate_quote():
    """Generate a quote from the collection"""
    return random.choice(QUOTES)

def update_quote_file(quote):
    """Update the daily_quotivation.md file with the new quote using Indian time"""
    # Get current time in Indian timezone (IST)
    india_tz = pytz.timezone('Asia/Kolkata')
    today = datetime.datetime.now(india_tz).strftime("%B %d, %Y")
    
    content = f"""# Quote of the Day - {today}

> \"{quote}\"

*Generated with ❤️ by Quotivation Bot Done By Shree*

---

"""
    
    # Create the file if it doesn't exist
    quote_file = Path("daily_quotivation.md")
    
    if quote_file.exists():
        # Read existing content and prepend new quote
        existing_content = quote_file.read_text()
        # Keep only the last 30 quotes to avoid the file growing too large
        quotes_list = existing_content.split('---\n\n')
        if len(quotes_list) > 30:
            quotes_list = quotes_list[:30]
        updated_content = content + '\n'.join(quotes_list[:-1]) if len(quotes_list) > 1 else content
        quote_file.write_text(updated_content)
    else:
        # Create new file with just today's quote
        quote_file.write_text(content)
    
    print(f"Updated daily_quotivation.md with quote for {today}")

def update_readme(quote, today):
    """Update the README.md file with the new quote"""
    readme_file = Path("README.md")
    if not readme_file.exists():
        print("README.md not found, skipping update.")
        return

    readme_content = readme_file.read_text()

    # Define the new quote section content
    new_quote_section = f"""## 📚 Example Quote\n\n```\n# Quote of the Day - {today}\n\n> \"{quote}\"\n\n*Generated with ❤️ by Quotivation Bot*\n```"""

    # Find the start and end of the existing example quote section
    # This assumes the structure is consistent as per the generated README.md
    start_marker = "## 📚 Example Quote"
    end_marker = "## 📄 License"

    start_index = readme_content.find(start_marker)
    end_index = readme_content.find(end_marker)

    if start_index != -1 and end_index != -1 and start_index < end_index:
        # Replace the old section with the new one
        before_section = readme_content[:start_index]
        after_section = readme_content[end_index:]
        updated_readme_content = before_section + new_quote_section + "\n\n" + after_section
        readme_file.write_text(updated_readme_content)
        print("Updated README.md with the latest quote.")
    else:
        print("Could not find the example quote section in README.md, skipping update.")

def main():
    # Ensure scripts directory exists
    Path("scripts").mkdir(exist_ok=True)
    
    # Generate and update quote
    quote = generate_quote()
    update_quote_file(quote)
    
    # Get current time in Indian timezone (IST) for README update
    india_tz = pytz.timezone('Asia/Kolkata')
    today = datetime.datetime.now(india_tz).strftime("%B %d, %Y")
    update_readme(quote, today)

if __name__ == "__main__":
    main()