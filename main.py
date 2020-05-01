import sublime
import sublime_plugin


class MarkCommand(sublime_plugin.TextCommand):

    def get_diff_index(self):
        return 0

    def get_diff_text(self):
        # get old file here
        # get new file here
        # return only the diff
        return (
            "## old code ##\r\n" +
            "return local * 2;\r\n" +
            "## old code ##\r\n"
        )

    def run(self, edit):
        index = self.get_diff_index()
        diff = self.get_diff_text()
        # find the localtion of the diff
        # self.view.show_popup(diff, sublime.HIDE_ON_MOUSE_MOVE_AWAY)
        self.view.insert(edit, index, diff)
