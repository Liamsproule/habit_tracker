import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from . import habit_core


class HabitApp(toga.App):
    def startup(self):
        # Main vertical container
        self.main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Heading
        heading = toga.Label(
            "Today's Habits",
            style=Pack(font_size=20, padding=(0, 0, 10, 0))
        )
        self.main_box.add(heading)

        # Box that will hold one Switch per habit
        self.checks_box = toga.Box(style=Pack(direction=COLUMN, flex=1))
        self.main_box.add(self.checks_box)

        # Build the switches
        self.switches = []
        for h in habit_core.HABITS:
            sw = toga.Switch(h)
            self.switches.append(sw)
            self.checks_box.add(sw)

        # Save button
        save_btn = toga.Button(
            "Save",
            on_press=self.save_results,
            style=Pack(padding_top=10)
        )
        self.main_box.add(save_btn)

        # Show the window
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

    # ---------- Callbacks ----------

    def save_results(self, widget):
        """Collect the on/off state of each switch and persist it."""
        results = [
            {"habit": sw.label, "done": sw.is_on}
            for sw in self.switches
        ]
        habit_core.save_result(results)

        done = sum(r["done"] for r in results)
        total = len(results)
        toga.Window.info_dialog(
            "Saved",
            f"You completed {done}/{total} habits today!"
        )


def main():
    return HabitApp("Habit Tracker", "com.yourname.habit")
