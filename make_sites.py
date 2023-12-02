from staticjinja import Site

if __name__ == "__main__":
    context = {'solution': False}
    site = Site.make_site(
        contexts=[
            ('plus_over_10.html', context),
            ],
        outpath='build'
    )
    site.render()