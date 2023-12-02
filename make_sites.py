from staticjinja import Site

if __name__ == "__main__":
    site = Site.make_site(
        contexts=[
            ('plus_over_10.html', {'solution': False}),
            ('index.html', {'solution': True}),
            ],
        outpath='docs'
    )
    site.render()