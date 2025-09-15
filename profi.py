# profile.py

class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack  # expects a list
        self.github_username = github_username
        self.fun_fact = fun_fact

    def introduce(self):
        return f"Hi, I'm {self.name}. I love {self.favorite_language} and my hobby is {self.hobby}. Fun fact: {self.fun_fact}"

    def show_stack(self):
        stack = ", ".join(self.tech_stack)
        return f"My tech stack includes: {stack}"

    def github_link(self):
        return f"https://github.com/{self.github_username}"


# ---- Example usage ----
if __name__ == "__main__":
    # Create your profile here
    my_profile = Profile(
        name="Shantal",
        favorite_language="Python",
        hobby="Reading tech blogs",
        tech_stack=["Python", "Django", "Git", "HTML", "CSS"],
        github_username="shantal-dev",
        fun_fact="I can debug faster with music on!"
    )

    # Call methods
    print(my_profile.introduce())
    print(my_profile.show_stack())
    print("GitHub Profile:", my_profile.github_link())

