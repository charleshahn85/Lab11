
from mindmap_leaf import MindMapLeaf
from mindmap_composite import MindMapComposite

def main():
    root = MindMapComposite("The Battle at Wolf 359", "circle")

    # Adding characters
    characters = MindMapComposite("Characters", "oval")
    characters.add(MindMapLeaf("Jean-Luc Picard / Locutus", "plain"))
    characters.add(MindMapLeaf("William Riker", "plain"))
    characters.add(MindMapLeaf("Data", "plain"))
    characters.add(MindMapLeaf("Worf", "plain"))
    characters.add(MindMapLeaf("Borg Queen (implied presence)", "plain"))
    root.add(characters)

    # Adding plot points
    plot_points = MindMapComposite("Plot Points", "square")
    plot_points.add(MindMapLeaf("Picard is assimilated by the Borg", "plain"))
    plot_points.add(MindMapLeaf("Riker takes command of the Enterprise", "plain"))
    plot_points.add(MindMapLeaf("The Federation fleet suffers heavy losses", "plain"))
    plot_points.add(MindMapLeaf("Enterprise crew devises a plan to stop the Borg", "plain"))
    root.add(plot_points)

    # Adding themes
    themes = MindMapComposite("Themes", "cloud")
    themes.add(MindMapLeaf("Identity and loss of self", "plain"))
    themes.add(MindMapLeaf("Duty and leadership", "plain"))
    themes.add(MindMapLeaf("Humanity vs. technology", "plain"))
    themes.add(MindMapLeaf("Collectivism vs. individuality", "plain"))
    root.add(themes)

    # Adding setting
    setting = MindMapComposite("Setting", "hexagon")
    setting.add(MindMapLeaf("USS Enterprise-D", "plain"))
    setting.add(MindMapLeaf("Wolf 359 (space battle location)", "plain"))
    setting.add(MindMapLeaf("Borg Cube", "plain"))
    setting.add(MindMapLeaf("Starfleet Command (background communication)", "plain"))
    root.add(setting)

    # Adding major conflicts
    conflicts = MindMapComposite("Major Conflicts", "bang")
    conflicts.add(MindMapLeaf("Federation vs. Borg (existential threat)", "plain"))
    conflicts.add(MindMapLeaf("Riker’s internal struggle as acting captain", "plain"))
    conflicts.add(MindMapLeaf("Enterprise's fight to save Picard from assimilation", "plain"))
    root.add(conflicts)

    # Adding dialogue highlights
    dialogue = MindMapComposite("Dialogue Highlights", "oval")
    dialogue.add(MindMapLeaf("“I am Locutus of Borg.”", "plain"))
    root.add(dialogue)

    # Display the mind map
    root.display()


if __name__ == "__main__":
    main()
