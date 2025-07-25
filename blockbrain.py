from blockbrain.tracker import BlockBrainTracker

def main():
    print("""
     ██████╗ ██████╗  ██████╗  ██████╗██╗  ██╗██████╗  █████╗ ██╗███╗   ██╗
    ██╔════╝██╔═══██╗██╔═══██╗██╔════╝██║ ██╔╝██╔══██╗██╔══██╗██║████╗  ██║
    ██║     ██║   ██║██║   ██║██║     █████╔╝ ██████╔╝███████║██║██╔██╗ ██║
    ██║     ██║   ██║██║   ██║██║     ██╔═██╗ ██╔═══╝ ██╔══██║██║██║╚██╗██║
    ╚██████╗╚██████╔╝╚██████╔╝╚██████╗██║  ██╗██║     ██║  ██║██║██║ ╚████║
     ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
                                 blockbrain v0.1
    -------------------------------------------------------------------------
    """)

    tracker = BlockBrainTracker()
    tracker.run()

if __name__ == "__main__":
    main()
