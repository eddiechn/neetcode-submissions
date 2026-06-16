class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> lookup = new HashMap<>(3);

        lookup.put(')', '(');
        lookup.put('}', '{');
        lookup.put(']', '[');

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (lookup.containsKey(c)) {
                if (!stack.isEmpty() && (lookup.get(c)).equals(stack.peek())) {
                    stack.pop();
                } 
                else return false;
            }

            else stack.push(c);
        }

        return stack.isEmpty();
        
    }
}
