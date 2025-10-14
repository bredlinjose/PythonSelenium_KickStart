import pandas as pd
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
class POMGenerator:

    pages_dir = os.path.join(project_root, "pages")
    def __init__(self, excel_path, output_dir=pages_dir):
        self.excel_path = excel_path
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

        # ✅ Ensure __init__.py exists
        init_file = os.path.join(self.output_dir, "__init__.py")
        if not os.path.exists(init_file):
            with open(init_file, "w") as f:
                f.write("# Package initializer for generated POM pages\n")

    def generate_pages_from_excel(self):
        # Load all sheets as a dictionary of DataFrames
        sheets = pd.read_excel(self.excel_path, sheet_name=None)

        for page_name, df in sheets.items():
            self.generate_page_class(page_name, df)

    def generate_page_class(self, page_name, df):
        class_name = f"{page_name.title().replace('_', '').replace(' ', '')}Page"
        file_name = f"{page_name.lower()}_page.py"
        file_path = os.path.join(self.output_dir, file_name)

        with open(file_path, "w") as f:
            # Imports
            f.write("from selenium.webdriver.common.by import By\n")
            f.write("from selenium.webdriver.remote.webdriver import WebDriver\n")
            f.write("from selenium.webdriver.support.ui import Select, WebDriverWait\n")
            f.write("from selenium.webdriver.support import expected_conditions as EC\n")
            f.write("from selenium.webdriver.common.action_chains import ActionChains\n")
            f.write("from selenium.webdriver.common.keys import Keys\n")
            f.write("from selenium.common.exceptions import TimeoutException\n\n")

            # Class declaration
            f.write(f"class {class_name}:\n")
            f.write("    def __init__(self, driver: WebDriver):\n")
            f.write("        self.driver = driver\n")
            f.write("        self.wait = WebDriverWait(driver, 10)\n")
            f.write("        self.actions = ActionChains(driver)\n")

            # Locators
            for _, row in df.iterrows():
                locator_name = row['locator_name']
                locator_type = row['locator_type']
                locator_value = row['locator']
                if pd.notna(locator_name) and pd.notna(locator_type) and pd.notna(locator_value):
                    escaped_value = str(locator_value).replace('"', '\\"')
                    f.write(f"        self.{locator_name} = (By.{locator_type.upper()}, \"{escaped_value}\")\n")
            f.write("\n")

            # Action Methods with Waits
            for _, row in df.iterrows():
                locator_name = row['locator_name']
                action = row['action']
                test_data = row['test_data'] if pd.notna(row['test_data']) else ""

                if pd.isna(action):
                    continue

                method_name = f"{action}_{locator_name}".lower()
                f.write(f"    def {method_name}(self):\n")

                if action == "click":
                    f.write(f"        element = self.wait.until(EC.element_to_be_clickable(self.{locator_name}))\n")
                    f.write(f"        element.click()\n")

                elif action == "send_keys":
                    f.write(
                        f"        element = self.wait.until(EC.visibility_of_element_located(self.{locator_name}))\n")
                    f.write(f"        element.clear()\n")
                    f.write(f"        element.send_keys(\"{test_data}\")\n")

                elif action == "is_displayed":
                    f.write(f"        try:\n")
                    f.write(
                        f"            element = self.wait.until(EC.visibility_of_element_located(self.{locator_name}))\n")
                    f.write(f"            return element.is_displayed()\n")
                    f.write(f"        except TimeoutException:\n")
                    f.write(f"            return False\n")

                elif action == "move_to_element":
                    f.write(f"        element = self.wait.until(EC.presence_of_element_located(self.{locator_name}))\n")
                    f.write(f"        self.actions.move_to_element(element).perform()\n")

                elif action == "scroll_to_element":
                    f.write(f"        element = self.wait.until(EC.presence_of_element_located(self.{locator_name}))\n")
                    f.write(f"        self.driver.execute_script(\"arguments[0].scrollIntoView(true);\", element)\n")

                elif action == "select_by_index":
                    f.write(f"        element = self.wait.until(EC.element_to_be_clickable(self.{locator_name}))\n")
                    f.write(f"        Select(element).select_by_index(int(\"{test_data}\"))\n")

                elif action == "select_by_visible_text":
                    f.write(f"        element = self.wait.until(EC.element_to_be_clickable(self.{locator_name}))\n")
                    f.write(f"        Select(element).select_by_visible_text(\"{test_data}\")\n")

                elif action == "page_down":
                    f.write(f"        element = self.wait.until(EC.presence_of_element_located(self.{locator_name}))\n")
                    f.write(f"        element.send_keys(Keys.PAGE_DOWN)\n")

                elif action == "page_up":
                    f.write(f"        element = self.wait.until(EC.presence_of_element_located(self.{locator_name}))\n")
                    f.write(f"        element.send_keys(Keys.PAGE_UP)\n")

                else:
                    f.write(f"        # Unsupported action: {action}\n")

                f.write("\n")


if __name__ == "__main__":
    excel_file_path = os.path.join(project_root, "test_data", "OrangeHRM.xlsx")

    pom_generator = POMGenerator(excel_file_path)
    pom_generator.generate_pages_from_excel()

