import PyQt6.QtWidgets as qtw
#import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg

class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dilution Calculator")

        layout = qtw.QFormLayout()

        validator = qtg.QDoubleValidator()

        self.solutionA = qtw.QLabel("Solution A:")
        self.initial_A_conc = qtw.QLabel("Molarity:")
        self.initial_A_vol = qtw.QLabel("Volume (mL):")

        self.solution_A_conc = qtw.QLineEdit("")
        self.solution_A_conc.setValidator(validator)

        self.solution_A_vol = qtw.QLineEdit("")
        self.solution_A_vol.setValidator(validator)

        self.solutionB = qtw.QLabel("Solution B:")
        self.initial_B_conc = qtw.QLabel("Molarity:")
        self.initial_B_vol = qtw.QLabel("Volume (mL):")
        
        self.solution_B_conc = qtw.QLineEdit("")
        self.solution_B_conc.setValidator(validator)

        self.solution_B_vol = qtw.QLineEdit("")
        self.solution_B_vol.setValidator(validator)

        self.final_A_conc = qtw.QLabel("Desired final conc. A (M):")
        self.final_B_conc = qtw.QLabel("Desired final conc. B (M):")
 
        self.final_conc_A = qtw.QLineEdit("")
        self.final_conc_B = qtw.QLineEdit("")

        self.final_vol = qtw.QLabel("Desired final vol. (mL):")
        self.final_volume = qtw.QLineEdit("")
        self.final_volume.setValidator(validator)

        self.button1 = qtw.QPushButton("Go")
        self.button1.clicked.connect(self.calculate)

        self.steps = qtw.QLabel("Fill in all boxes and press go to get instructions")

        layout.addRow(self.solutionA)
        layout.addRow(self.initial_A_conc, self.initial_A_vol)
        layout.addRow(self.solution_A_conc, self.solution_A_vol)

        layout.addRow(self.solutionB)
        layout.addRow(self.initial_B_conc, self.initial_B_vol)
        layout.addRow(self.solution_B_conc, self.solution_B_vol)

        layout.addRow(self.final_A_conc, self.final_B_conc)
        layout.addRow(self.final_conc_A, self.final_conc_B)

        layout.addRow(self.final_vol)
        layout.addRow(self.final_volume)

        layout.addRow(self.button1)

        layout.addRow(self.steps)

        widget = qtw.QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)

    def calculate(self):
        try:
            # Reading values from input fields and converting to floats
            initial_conc_A = float(self.solution_A_conc.text())
            initial_conc_B = float(self.solution_B_conc.text())
            final_conc_A = float(self.final_conc_A.text())
            final_conc_B = float(self.final_conc_B.text())
            final_volume_mL = float(self.final_volume.text())


            print(f"initial_conc_A: {initial_conc_A}, initial_conc_B: {initial_conc_B}\nfinal_conc_A: {final_conc_A}, final_conc_B: {final_conc_B}\nfinal_volume_mL: {final_volume_mL}")

            # Calculate final moles needed for each solution
            final_A_moles = final_conc_A * (final_volume_mL / 1000)
            final_B_moles = final_conc_B * (final_volume_mL / 1000)
            
            print(f"final_A_moles: {final_A_moles}")
            print(f"final_B_moles: {final_B_moles}")


            # Determine the required volume from stock solutions
            vol_from_stock_A = (final_A_moles / initial_conc_A) * 1000
            vol_from_stock_B = (final_B_moles / initial_conc_B) * 1000
            print(f"vol_from_stock_A: {vol_from_stock_A}")
            print(f"vol_from_stock_B: {vol_from_stock_B}")

            # Calculate the amount of water needed to dilute to the final volume
            total_vol_from_stocks = vol_from_stock_A + vol_from_stock_B
            water_vol = final_volume_mL - total_vol_from_stocks

            # Validate the water volume
            if water_vol < 0:
                self.steps.setText("Error: Not enough room for desired concentration. Adjust final volume or concentration.")
            else:
                self.steps.setText(f"Steps:\n1) Combine {vol_from_stock_A:.2f} mL of solution A and {vol_from_stock_B:.2f} mL of solution B.\n"
                                   f"2) To reach a final volume of {final_volume_mL} mL, add {water_vol:.2f} mL of deionized water.")
        except ValueError:
            self.steps.setText("Please fill in all fields with valid numbers.")

app = qtw.QApplication([])

window = MainWindow()
window.show()

app.exec()



        