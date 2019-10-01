class Solution {
    public int lengthLongestPath(String input) {
        String[] components = input.split("\n");
        int[] levels = new int[components.length];
        process(components, levels);

        int start = 0;
        List<PathNode> roots = new ArrayList<PathNode>();
        while (start < components.length) {
            PathNode root = new PathNode(components[start], 0);
            roots.add(root);
            start = buildTree(root, components, levels, start + 1);
        }
        int ret = -2;

        for (PathNode root : roots) {
            int candidate = longestPathLength(root);
            if (candidate > ret)
                ret = candidate;
        }

        if (ret > 0)
            return ret;
        else
            return 0;
    }

    private int buildTree(PathNode node, String[] components, int[] levels, int i) {
        int level = node.level;
        while (i < components.length && levels[i] == level + 1) {
            PathNode child = new PathNode(components[i], level + 1);
            node.children.add(child);
            i = buildTree(child, components, levels, i + 1);
        }

        return i;
    }

    private void process(String[] components, int[] levels) {
        for (int i = 0; i < components.length; i++) {
            String component = components[i];

            if (component.length() > 4 && component.charAt(0) == ' ' && component.charAt(1) == ' ' && component.charAt(2) == ' ' && component.charAt(3) == ' ') {
                levels[i] = 1;
                components[i] = component.substring(4);
            }
            else {
                int j = 0;

                while (j < component.length()) {
                    if (component.charAt(j) == '\t')
                        j += 1;
                    else
                        break;
                }

                levels[i] = j;
                components[i] = component.substring(j);
            }
        }
    }

    private int longestPathLength(PathNode node) {
        if (node == null)
            return 0;

        if (node.children.size() == 0) {
            String name = node.name;

            if (name.indexOf(".") != -1)
                return name.length();
            else
                return -2;
        }

        int ret = -1;
        for (PathNode child : node.children) {
            int candidate = 1 + longestPathLength(child);
            if (candidate > ret)
                ret = candidate;
        }

        if (ret >= 0)
            return ret + node.name.length();
        return -2;
    }

    private class PathNode {
        public String name;
        public int level;
        public List<PathNode> children;

        public PathNode(String name, int level) {
            this.name = name;
            this.level = level;
            children = new ArrayList<PathNode>();
        }
    }

}
