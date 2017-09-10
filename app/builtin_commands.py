from random import shuffle

from app.commands import (
    Command,
    Commands,
)


class CommandGroup(object):
    def __init__(self, name, *commands):
        self.name = name
        self.commands = sorted(commands)


    def __lt__(self, other):
        return self.name < other.name


builtin_command_groups = [
    CommandGroup(
        'Web Search',
        Command(
            name='g',
            description='Google search',
            url_pattern='https://www.google.com/search?q={0}',
        ),
    ),

    CommandGroup(
        'Maps',
        Command(
            name='gm',
            description='Google Maps search',
            url_pattern='https://www.google.com/maps/search/{0}',
        ),
    ),

    CommandGroup(
        'Images',
        Command(
            name='gi',
            description='Google Images search',
            url_pattern='https://www.google.com/search?tbm=isch&q={0}',
        ),
    ),

    CommandGroup(
        'News',
        Command(
            name='nyt',
            description='Go to New York Times',
            url_pattern=('hhttps://query.nytimes.com/search/sitesearch/?action=click&contentCollection&region=TopBar&WT.nav=searchWidget&module=SearchSubmit&pgtype=Homepage#/asdf/7days://query.nytimes.com/search/sitesearch/?action=click&contentCollection&region=TopBar&WT.nav=searchWidget&module=SearchSubmit&pgtype=Homepage#/{0}/7days/'),
            default_url='https://www.nytimes.com',
        ),
        Command(
            name='wa',
            description='Query Wolfram|Alpha',
            url_pattern='https://www.wolframalpha.com/input/?i={0}',
            default_url='https://www.wolframalpha.com',
        ),
        Command(
            name='r',
            description='Search all Reddit subreddits',
            url_pattern='https://www.reddit.com/search?q={0}',
            default_url='https://www.reddit.com',
        ),
        Command(
            name='rr',
            description=('Search a specific Reddit subreddit, '
                         'subreddit name is the first argument to rr'),
            url_pattern=('https://www.reddit.com/r/{1}/search?q={2:}'
                         '&restrict_sr=on'),
            default_url='https://www.reddit.com',
        ),
    ),

    CommandGroup(
        'Social',
        Command(
            name='fb',
            description='Facebook search',
            url_pattern='https://www.facebook.com/search/top/?q={0}',
            default_url='https://www.facebook.com',
        ),
        Command(
            name='in',
            description='Google Inbox search',
            url_pattern='https://inbox.google.com/search/{0}',
            default_url='https://www.inbox.google.com',
        ),
    ),

    CommandGroup(
        'Entertainment',
        Command(
            name='yt',
            description='Youtube search',
            url_pattern='https://www.youtube.com/results?search_query={0}',
        ),
        Command(
            name='ig',
            description='Instagram search',
            url_pattern='https://www.instagram.com/{0}',
            default_url='https://www.instagram.com',
        ),
        Command(
            name='sp',
            description='Spotify search',
            url_pattern='https://open.spotify.com/search/results/{0}',
            default_url='https://www.open.spotify.com',
        ),
        Command(
            name='yp',
            description='Yelp search',
            url_pattern='http://www.yelp.com/search?find_desc={0}&src=opensearch',
            default_url='https://www.yelp.com',
        ),
    ),

    CommandGroup(
        'Shopping',
        Command(
            name='a',
            description='Amazon search.',
            url_pattern='https://www.amazon.com/s?field-keywords={0}'
        ),
        Command(
            name='eb',
            description='Ebay search.',
            url_pattern='http://rover.ebay.com/rover/1/711-47294-18009-3/4?mfe=search&mpre=http://www.ebay.com/sch/i.html?_nkw={0}'
        ),
    ),

    CommandGroup(
        'Stocks & Markets',
        Command(
            name='gf',
            description='Google Finance search',
            url_pattern='https://www.google.com/finance?q={0}',
        ),
        Command(
            name='yf',
            description='Go to stock on Yahoo Finance',
            url_pattern='https://finance.yahoo.com/quote/{0}',
            default_url='https://finance.yahoo.com/',
        ),
    ),

    CommandGroup(
        'For Developers',
        Command(
            name='gw',
            description='Google search without w3schools results',
            url_pattern='https://www.google.com/search?q={0}%20-w3schools'
        ),
        Command(
            name='so',
            description='Search StackOverflow and StackExhange on Google',
            url_pattern=('https://www.google.com/search?q={0}%20'
                         'site%3Astackoverflow.com%20OR%20'
                         'site%3Astackexchange.com%20OR%20'
                         'site%3Asuperuser.com%20OR%20'
                         'site%3Aserverfault.com%20OR%20'
                         'site%3Aaskubuntu.com'),
            default_url='https://stackoverflow.com',
        ),
        Command(
            name='gh',
            description='Search Github',
            url_pattern=('https://github.com/search?q={0}&ref=opensearch'),
            default_url='https://github.com/williammlu',
        ),
        Command(
            name='hs',
            description='Hoogle (Haskell) search',
            url_pattern='https://www.haskell.org/hoogle/?hoogle={0}',
        ),
        Command(
            name='man',
            description='Search Linux man pages on Google',
            url_pattern=('https://www.google.com/search?q={0}%20'
                         'site%3Aman7.org/linux/man-pages'),
            default_url='http://man7.org/linux/man-pages/index.html',
        ),
        Command(
            name='cpp',
            description='C++ standard library search.',
            url_pattern=('http://www.cppreference.com/mwiki/index.php?search='
                         '{0|percent_decode|percent_encode_plus|percent_decode}'),
            default_url='http://www.cppreference.com',
        ),
        Command(
            name='ascii',
            description='ASCII table',
            url_pattern='http://web.cs.mun.ca/~michael/c/ascii-table.html',
        ),
        Command(
            name='uni',
            description='Unicode viewer',
            url_pattern='https://r12a.github.io/uniview',
        ),
        Command(
            name='unic',
            description='Unicode code converter',
            url_pattern='https://r12a.github.io/apps/conversion',
        ),
        Command(
            name='time',
            description='Current Unix timestamp and more',
            url_pattern='https://www.epochconverter.com',
        ),
        Command(
            name='php',
            description='PHP manual search',
            url_pattern='https://secure.php.net/manual-lookup.php?pattern={0}',
            default_url='https://secure.php.net/manual/en/index.php',
        ),
        Command(
            name='go',
            description='golang.org search',
            url_pattern='https://golang.org/search?q={0}',
            default_url='https://golang.org',
        ),
        Command(
            name='rs',
            description='Rust standard library search',
            url_pattern='https://doc.rust-lang.org/std/?search={0}',
            default_url='https://www.rust-lang.org/documentation.html',
        ),
        Command(
            name='rb',
            description='Search docs.ruby-lang.org on Google',
            url_pattern=('https://www.google.com/search?q={0}%20'
                         'site%3Adocs.ruby-lang.org/en'),
            default_url='https://docs.ruby-lang.org/en',
        ),
        Command(
            name='py',
            description='Search docs.python.org on Google',
            url_pattern=('https://www.google.com/search?q={0}%20'
                         'site%3Adocs.python.org'),
            default_url='https://docs.python.org',
        ),
                Command(
            name='np',
            description='Search docs.scipy.org on Google',
            url_pattern=('https://www.google.com/search?q={0}%20'
                         'site%3Adocs.scipy.org'),
            default_url='https://docs.scipy.org',
        ),
        Command(
            name='js',
            description='Search developer.mozilla.org for Javascript on Google',
            url_pattern=('https://www.google.com/search?q={0}%20javascript%20'
                         'site%3Adeveloper.mozilla.org'),
            default_url='https://developer.mozilla.org/en-US/docs/Web/JavaScript',
        ),
        Command(
            name='npm',
            description='Search npm',
            url_pattern='https://www.npmjs.com/search?q={0}',
            default_url='https://www.npmjs.com',
        ),
        Command(
            name='ios',
            description=('Search developer.apple.com/reference (iOS, '
                         'Objective-C, Swift, etc.) on Google'),
            url_pattern=('https://www.google.com/search?q={0}%20'
                         'site%3Adeveloper.apple.com/reference'),
            default_url='https://developer.apple.com/reference',
        ),
        Command(
            name='dn',
            description=('Search docs.microsoft.com/en-us/dotnet (.NET) '
                         'on Google'),
            url_pattern=('https://www.google.com/search?q={0}%20'
                         'site%3Adocs.microsoft.com/en-us/dotnet'),
            default_url='https://docs.microsoft.com/en-us/dotnet',
        ),
        Command(
            name='an',
            description='Search Android API',
            url_pattern=('https://www.google.com/search?q={0}%20'
                         'site%3Adeveloper.android.com/reference'),
            default_url='https://developer.android.com/reference',
        ),
        Command(
            name='ja',
            description='Search Java 8 API',
            url_pattern=('https://www.google.com/search?q={0}%20'
                         'site%3Adocs.oracle.com/javase/8/docs'),
            default_url='https://docs.oracle.com/javase/8/docs',
        ),
        Command(
            name='cron',
            description='cron explainer',
            url_pattern=('http://crontab.guru/#'
                         '{1|percent_decode}_'
                         '{2|percent_decode}_'
                         '{3|percent_decode}_'
                         '{4|percent_decode}_'
                         '{5|percent_decode}'),
            default_url='http://crontab.guru/',
        ),
    ),

    CommandGroup(
        'Miscellaneous',
        Command(
            name='fedex',
            description='Track Fedex package',
            url_pattern='https://www.fedex.com/apps/fedextrack/?tracknumbers={0}',
            default_url='https://www.fedex.com',
        ),
        Command(
            name='ups',
            description='Track UPS package',
            url_pattern='https://wwwapps.ups.com/WebTracking/track?track=yes&trackNums={0}',
            default_url='https://www.ps.com',
        ),
        Command(
            name='dhl',
            description='Track DHL package',
            url_pattern='http://www.dhl.com/en/express/tracking.html?AWB={0}',
            default_url='http://www.dhl.com',
        ),
        Command(
            name='usps',
            description='Track USPS parcel',
            url_pattern='https://tools.usps.com/go/TrackConfirmAction?tLabels={0}',
            default_url='https://www.usps.com',
        ),
        Command(
            name='gd',
            description='Google Domains search',
            url_pattern='https://domains.google.com/registrar?s={0}',
        ),
        Command(
            name='gt',
            description='Translate to English with Google Translate',
            url_pattern='https://translate.google.com/#auto/en/{0}',
        ),
    ),
]
builtin_command_groups

builtin_commands = Commands(
    [
        command
        for command_group in builtin_command_groups
        for command in command_group.commands
    ],
)


class SampleQuery(object):
    def __init__(self, command, comment, args=''):
        self.command = command
        self.args = args
        self.query = command + ' ' + args
        self.comment = comment


sample_queries = [
    SampleQuery(
        command='so',
        args='how to parse html with regexes',
        comment=('Search StackOverflow and StackExchange on Google to '
                 'find out how you can parse HTML with regexes.'),
    ),
    SampleQuery(
        command='rt',
        args='Ex Machina',
        comment='Search Rotten Tomatoes for Ex Machina.',
    ),
    SampleQuery(
        command='ascii',
        comment='Go to an ASCII table.',
    ),
    SampleQuery(
        command='cron',
        args='*/30 * 3 7 FRI',
        comment='Deciper the cron expression.',
    ),
    SampleQuery(
        command='wa',
        args='\xcf\x80 series representations'.decode('utf-8'),
        comment=('Find out which series converge to \xcf\x80 on '
                 'Wolfram|Alpha').decode('utf-8'),
    ),
    SampleQuery(
        command='w',
        args='rope data structure',
        comment='Search ropes on Wikipedia.',
    ),
]

def get_sample_queries():
    sample_queries_copy = sample_queries[:]
    shuffle(sample_queries_copy)
    return sample_queries_copy
