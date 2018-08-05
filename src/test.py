import os, sys, subprocess
from PyQt5.QtCore import QProcess
from PyQt5.QtCore import QTimer
import PyQt5.QtCore as QtCore
from PyQt5.QtWidgets import *#QScrollArea, QVBoxLayout, QGridLayout, QTabWidget, QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit, QLabel, QLineEdit, QFrame, QComboBox, QCheckBox, QInputDialog, QLineEdit
from subprocess import Popen, PIPE

home = os.environ['HOME'] 
os.environ['EOS_SOURCE'] = home + "/eos"
os.environ['EOS_NODEOS'] = home + "/.local/share/eosio/nodeos/"
os.environ['EZEOS_SOURCE'] = home + "/eclipse-workspace/ezeos/src"

class BlockChain():
    class Block():
        def __init__(self):
            self.number = "1"
    def __init__(self):
        self.net = ['main', 'test', 'local']
        self.block = self.Block()
        self.running = False
        self.producer = ""
        self.testProducer = ""
        self.producerList =     [
                                    'https://api.eosnewyork.io:443', 
                                    'https://api.eosdetroit.io:443',
                                    'https://eos.greymass.com:443',
                                    'https://api.eosmetal.io:18890',
                                    'http://api.hkeos.com:80',
                                    'https://eosapi.blockmatrix.network:443',
                                    'https://fn.eossweden.se:443',
                                    'http://api.blockgenicbp.com:8888',
                                    'http://mainnet.eoscalgary.io:80',
                                    'http://mainnet.eoscalgary.io:80',
                                    'https://node1.eosphere.io',
                                    'https://eos.saltblock.io',
                                    'http://eos-api.worbli.io:80',
                                    'https://eos-api.worbli.io:443',
                                    'http://mainnet.eoscalgary.io:80',
                                    'https://user-api.eoseoul.io:443',
                                    'http://user-api.eoseoul.io:80', 
                                    'https://node2.liquideos.com:8883',
                                    'http://node2.liquideos.com:8888',
                                    'https://api.eosuk.io:443',
                                    'http://api1.eosdublin.io:80',
                                    'http://api.eosvibes.io:80',
                                    'http://api.cypherglass.com:8888',
                                    'https://api.cypherglass.com:443',
                                    'http://bp.cryptolions.io:8888',
                                    'http://dc1.eosemerge.io:8888',
                                    'https://dc1.eosemerge.io:5443',
                                    'https://api.eosio.cr:443',
                                    'https://api.eosn.io',
                                    'https://eu1.eosdac.io:443',
                                ]
        self.testProducerList = [
                                     'eosgreen.uk.to:9875',
                                     'ctestnet.edenx.io:62071',
                                     '54.194.49.21:9875',
                                     'superhero.cryptolions.io:9885',
                                     'venom.eoscalgary.com:9877',
                                     'joker.superhero.eos.roelandp.nl:9873',
                                     'ctestnet.eosdetroit.com:1339',
                                     'bp7-d3.eos42.io:9876',
                                     'superheroes.eosio.africa:9876',
                                     '156.38.160.91:9876',
                                     '166.70.202.194:9877',
                                     '18.188.52.250:9889',
                                     'ctest.eosnewyork.io:9870',
                                     '35.195.161.56:9876',
                                     '159.89.197.162:9877',
                                     'dawn3-seed.tokenika.io:9876',
                                     'bp.blockgenic.io:9876',
                                     '47.52.18.70:9876',
                                     '120.27.130.60:9876',
                                     'ctest.koreos.io:9876',
                                     'ctestnet.objectcomputing.com:9876',
                                     'test.eosys.io:9875',
                                     'bp-test.eosasia.one:9876',
                                     '138.68.15.85:9876',
                                     '47.88.222.80:9876',
                                     '54.233.222.22:9875',
                                     '39.108.231.157:9877',
                                     'ctestnet.eoshenzhen.io:9876',
                                     'eosbp.enjoyshare.net:9876',
                                     'bpt1.eosbixin.com:9876',
                                     '46.4.253.242:7610',
                                     'superhero-bp1.eosphere.io:9876',
                                     '138.68.238.129:9875',
                                     '178.49.174.48:9876',
                                     'superhero.worbli.io:9876',
                                     'wonderwoman.eosreal.io:9876',
                                     'eosbrazil.com:9878',
                                     '35.202.41.160:9876',
                              ]

class Wallet():
    
    def __init__(self):
        self.name = ""
        self.key = ""
        self.ownerPrivateKey = ""
        self.ownerPublicKey = ""
        self.activePrivateKey = ""
        self.activePublicKey = ""
        self.locked = False
        self.url = "http://localhost:8888"
        
    def reset(self):
        self.name = ""
        self.key = ""
        self.ownerPrivateKey = ""
        self.ownerPublicKey = ""
        self.activePrivateKey = ""
        self.activePublicKey = ""
        self.locked = False
    
    def testFunction(self):
        self.testEncryption()
        print('testfunc')
    
    
class Account():
    
    def __init__(self):
        self.name = ""
        self.creator = ""
        self.owner = ""
        self.receiver = ""
        self.creatorOwnerKey = ""
        self.creatorActiveKey = ""
        self.eosioPublicKey = "EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV"
        self.eosioPrivateKey = "5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"
                            
    def reset(self):
        self.name = ""
    
class Order():
    def __init__(self):
        self.to = ""
        self.amount = 0.0000
        self.contract = ""
        self.currency = ""
        self.contractAccountName = ""
        self.stakeCPU = ""
        self.stakeBandWidth = ""
        self.buyRam = 0
    def reset(self):
        self.to = ""
        self.amount = 0.0000
        self.contract = ""
        self.currency = ""
        self.contractAccountName = ""

class GUI(QProcess):
    
    def __init__(self, parent=None):
        super(GUI, self).__init__(parent=None)
        self.wallet = Wallet()
        self.order = Order()
        self.account = Account()
        self.blockchain = BlockChain()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_label)
        self.timer.start(100)  
        
         
        # Create an instance variable here (of type QTextEdit)
        self.startBtn = QPushButton('OK')
        self.stopBtn = QPushButton('Cancel')
        self.label2 = QLabel("Test Net")
        self.label = QLabel("Main Net")
        self.setPermissionObjectButton = QPushButton("Set Permission Object")
        self.stakeBandwidthButton = QPushButton("Stake bandwidth")
        self.testEncryptionButton = QPushButton("TestEncryption")
        self.TestFunctionButton = QPushButton("TestFunction")
        self.createEosioWalletButton = QPushButton("Create Eosio Wallet and account")
        self.createEosioTokenAccountButton = QPushButton("Create eosio.token wallet and account")
        self.openContractButton = QPushButton("Open Contract")    
        self.setWalletNameButton = QPushButton("Wallet Name") 
        self.openWalletNameButton = QPushButton("Open Wallet") 
        self.setWalletPublicKeysButton = QPushButton("Set Wallet Public Keys")
        self.restartButton = QPushButton("Reset Local Chain")
        self.startButton = QPushButton("Start Local Chain")
        self.stopButton = QPushButton("Stop Local Chain")
        self.flushButton = QPushButton("Rename wallet directory")
        self.createWalletButton = QPushButton("Create Wallet")
        self.setOwnerKeyButton = QPushButton("Create Owner Keys")
        self.setActiveKeyButton = QPushButton("Create Active Keys")
        self.importKeysButton = QPushButton("Import Keys To Wallet")
        self.setAccountNameButton = QPushButton("Account Name")
        self.setAccountOwnerButton = QPushButton("Account Owner")
        self.setCreatorAccountNameButton = QPushButton("Creator Account Name")
        self.setStakeCPUAmountButton = QPushButton("Stake CPU amount")
        self.setStakeBandWidthAmountButton = QPushButton("Stake Bandwidth amount")
        self.buyRAMButton = QPushButton("Buy RAM")
        self.setBuyRAMAmountButton = QPushButton("Set RAM Amount")
        self.createAccountButton = QPushButton("Create Account")
        self.setSendAmountButton = QPushButton("Set Send Amount")
        self.setSendRecipientAccountButton = QPushButton("Set Recipient Account")
        self.sendAmountButton = QPushButton("Send Funds")
        frameStyle = QFrame.Sunken | QFrame.StyledPanel        
        self.getInfoLabel = QLabel()
        self.getInfoLabel.setFrameStyle(frameStyle)
        self.walletNameLabel = QLabel()
        self.walletNameLabel.setFrameStyle(frameStyle)
        self.accountNameLabel = QLabel()
        self.accountNameLabel.setFrameStyle(frameStyle)
        self.contractNameLabel = QLabel()
        self.contractNameLabel.setFrameStyle(frameStyle)
        self.creatorNameLabel = QLabel()
        self.creatorNameLabel.setFrameStyle(frameStyle)      
        self.openFileNameButton = QPushButton("Load Contract")
        self.loadEosioContractButton = QPushButton("Load EosioContract")
        self.issueButton = QPushButton("Issue Currency")
        self.recipientNameButton = QPushButton("Set Recipient Name")
        self.amountButton = QPushButton("Amount")
        self.issueToAccountButton = QPushButton("Issue To Account")
        self.transferToAccountButton = QPushButton("Transfer To Account")
        self.chooseCurrencyButton = QPushButton("Set Token Name")
        self.getInfoButton = QPushButton("Get Info")        
        self.getBalanceButton = QPushButton("Get Balance")    
        self.getAccountDetailsButton = QPushButton("Get Account Details")
       
        self.listWalletsButton = QPushButton("List Wallets")
        self.getBlockInfoButton = QPushButton("Block Info")
        self.setBlockNumberButton = QPushButton("Set Block Number")
        self.getActionsButton = QPushButton("Get Actions")
        self.showKeysButton = QPushButton("Show Keys")
        self.listProducersButton = QPushButton("Get Block Producers")
        self.getProducerInfoButton = QPushButton("Get Block Producer Info")
        self.producerBox = QComboBox()
        self.testProducerBox = QComboBox()
        self.producerBox.setObjectName(("Access to Main Net"))
        self.testProducerBox.setObjectName(("Access To Test Net"))
        self.toggleMainNet = QCheckBox("Main Net")
        self.toggleTestNet = QCheckBox("Test Net")
        self.toggleLocalNet = QCheckBox("Local Net")
#         for i in blockchain.producerList:
#             self.producerBox.addItem(i)
#         for i in blockchain.testProducerList:
#             self.testProducerBox.addItem(i)
        self.setPermissionObjectButton.clicked.connect(self.setPermissionObject)
        self.TestFunctionButton.clicked.connect(self.wallet.testFunction)
        self.toggleMainNet.toggled.connect(self.mainNet)
        self.toggleTestNet.toggled.connect(self.testNet)
        self.toggleLocalNet.toggled.connect(self.localNet)
        self.toggleWalletLock = QCheckBox("Lock Wallet")
        self.toggleWalletLock.toggled.connect(self.lockWallet)
        self.listProducersButton.clicked.connect(self.listProducers)
        self.testEncryptionButton.clicked.connect(self.testEncryption) 
        self.setWalletPublicKeysButton.clicked.connect(self.setWalletPublicKeys)
        self.listWalletsButton.clicked.connect(self.listWallets)
        self.getBalanceButton.clicked.connect(self.getBalance)    
        self.getAccountDetailsButton.clicked.connect(self.getAccountDetails)
        self.getInfoButton.clicked.connect(self.getInfo)
        self.stopButton.clicked.connect(self.stopChain)
        self.startButton.clicked.connect(self.startChain)
        self.restartButton.clicked.connect(self.resetChain)    
        self.setWalletNameButton.clicked.connect(self.setWalletName)
        self.openWalletNameButton.clicked.connect(self.openWalletName)
        self.createWalletButton.clicked.connect(self.createWallet)
        self.setOwnerKeyButton.clicked.connect(self.setOwnerKey)
        self.setActiveKeyButton.clicked.connect(self.setActiveKey)
        self.importKeysButton.clicked.connect(self.importKeys)
        self.setAccountNameButton.clicked.connect(self.createAccountName)
        self.setAccountOwnerButton.clicked.connect(self.setAccountOwner) 
        self.setCreatorAccountNameButton.clicked.connect(self.createCreatorAccountName)
        self.setStakeCPUAmountButton.clicked.connect(self.setStakeCPUAmount)
        self.setStakeBandWidthAmountButton.clicked.connect(self.setStakeBandWidthAmount)
        self.setBuyRAMAmountButton.clicked.connect(self.setBuyRAMAmount)
        self.buyRAMButton.clicked.connect(self.buyRAM)
        self.createAccountButton.clicked.connect(self.createAccount)
        self.openContractButton.clicked.connect(self.LoadContract)
        self.openFileNameButton.clicked.connect(self.setContractSteps)
        self.issueButton.clicked.connect(self.issueCurrency)
        self.flushButton.clicked.connect(self.flushWallets)
        self.amountButton.clicked.connect(self.setAmount)
        self.recipientNameButton.clicked.connect(self.setRecipientName)
        self.issueToAccountButton.clicked.connect(self.issueToAccount)
        self.transferToAccountButton.clicked.connect(self.transferToAccount)
        self.chooseCurrencyButton.clicked.connect(self.chooseCurrency)
        self.getBlockInfoButton.clicked.connect(self.getBlockInfo)
        self.setBlockNumberButton.clicked.connect(self.setBlockNumber)
        self.getActionsButton.clicked.connect(self.getActions)
        self.showKeysButton.clicked.connect(self.showKeys)
        self.listProducersButton.clicked.connect(self.listProducers)
        self.getProducerInfoButton.clicked.connect(self.getProducerInfo)
        self.setSendAmountButton.clicked.connect(self.setSendAmount)
        self.setSendRecipientAccountButton.clicked.connect(self.setRecipientAccount) 
        self.sendAmountButton.clicked.connect(self.sendToAccount)
        self.loadEosioContractButton.clicked.connect(self.loadEosioContract)
        self.createEosioWalletButton.clicked.connect(self.createEosioWallet)
        self.createEosioTokenAccountButton.clicked.connect(self.createEosioTokenAccount)
        self.stakeBandwidthButton.clicked.connect(self.stakeBandwidth)
        self.native = QCheckBox()
        self.native.setText("EZEOS")
        self.native.setChecked(True)
        if sys.platform not in ("win32", "darwin"):
            self.native.hide()
        self.layout = QGridLayout()
        self.hbox = QHBoxLayout()
       

        self.edit = QTextEdit()
        self.edit.setWindowTitle("QTextEdit Standard Output Redirection")

        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)

        #self.vbox.addLayout(self.hbox2)
        self.vbox.addWidget(self.edit)
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.layout)
        self.central = QWidget()

        self.central.setLayout(self.vbox)
        self.central.show()

        self.startBtn.clicked.connect(self.startNodeos)
        self.stopBtn.clicked.connect(self.kill)
        self.stateChanged.connect(self.slotChanged)

        
        
        self.layout.addWidget(self.getInfoLabel,  0, 0, 1, 7)
     
        
        self.tabs = QTabWidget()
        self.tab1 = QWidget()    
        self.tab2 = QWidget()
        self.tab3 = QWidget()    
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()
        self.tabs.resize(200,2000) 
 
       
        self.tabs.addTab(self.tab1,"Block chain")
        self.tabs.addTab(self.tab2,"Wallets")
        self.tabs.addTab(self.tab3,"Accounts")
        self.tabs.addTab(self.tab4,"Contract")
        self.tabs.addTab(self.tab5,"eosio.token")
        self.tabs.addTab(self.tab6,"test")
        
        self.tab1.layout = QVBoxLayout()
        self.tab1.layout.addWidget(self.stopButton)
        self.tab1.layout.addWidget(self.restartButton)
        self.tab1.layout.addWidget(self.startButton) 
        self.tab1.layout.addWidget(self.getBlockInfoButton)
        self.tab1.layout.addWidget(self.setBlockNumberButton)
        self.tab1.layout.addWidget(self.listProducersButton)
        self.tab1.layout.addWidget(self.toggleMainNet)
        self.tab1.layout.addWidget(self.toggleTestNet)
        self.tab1.layout.addWidget(self.toggleLocalNet)
        
        self.tab1.layout.addWidget(self.label)
        self.tab1.layout.addWidget(self.producerBox)
        self.tab1.layout.addWidget(self.label2)
        self.tab1.layout.addWidget(self.testProducerBox)
        self.tab1.layout.addWidget(self.getProducerInfoButton)            
        self.tab1.setLayout(self.tab1.layout)
 
       
        self.tab2.layout = QVBoxLayout()
        self.tab2.layout.addWidget(self.walletNameLabel)
        self.tab2.layout.addWidget(self.createEosioWalletButton)
        self.tab2.layout.addWidget(self.flushButton)
        self.tab2.layout.addWidget(self.setWalletNameButton)
        self.tab2.layout.addWidget(self.openWalletNameButton)
        self.tab2.layout.addWidget(self.createWalletButton)
        self.tab2.layout.addWidget(self.listWalletsButton)
        self.tab2.layout.addWidget(self.setOwnerKeyButton)
        self.tab2.layout.addWidget(self.setActiveKeyButton)
        self.tab2.layout.addWidget(self.importKeysButton)
        self.tab2.layout.addWidget(self.setWalletPublicKeysButton)
        self.tab2.layout.addWidget(self.showKeysButton)
        self.tab2.layout.addWidget(self.toggleWalletLock)
        self.tab2.setLayout(self.tab2.layout)

        self.tab3.layout = QVBoxLayout()
        self.tab3.layout.addWidget(self.accountNameLabel)
        self.tab3.layout.addWidget(self.creatorNameLabel)  
        self.tab3.layout.addWidget(self.setAccountNameButton)
        self.tab3.layout.addWidget(self.setAccountOwnerButton)
        self.tab3.layout.addWidget(self.setCreatorAccountNameButton)
        self.tab3.layout.addWidget(self.setStakeCPUAmountButton)
        self.tab3.layout.addWidget(self.setStakeBandWidthAmountButton)
        self.tab3.layout.addWidget(self.setBuyRAMAmountButton)
        self.tab3.layout.addWidget(self.buyRAMButton)
        self.tab3.layout.addWidget(self.createAccountButton)
        self.tab3.layout.addWidget(self.setSendAmountButton)
        self.tab3.layout.addWidget(self.setSendRecipientAccountButton)
        self.tab3.layout.addWidget(self.sendAmountButton)
        self.tab3.layout.addWidget(self.getAccountDetailsButton)
        self.tab3.layout.addWidget(self.getActionsButton)
        self.tab3.layout.addWidget(self.getBalanceButton)
        self.tab3.layout.addWidget(self.createEosioTokenAccountButton)
        self.tab3.layout.addWidget(self.stakeBandwidthButton)
        self.tab3.setLayout(self.tab3.layout) 
        
        self.tab4.layout = QVBoxLayout()
        self.tab4.layout.addWidget(self.contractNameLabel)
        self.tab4.layout.addWidget(self.loadEosioContractButton) 
        self.tab4.layout.addWidget(self.openContractButton)
        self.tab4.layout.addWidget(self.openFileNameButton)
        self.tab4.setLayout(self.tab4.layout)
    
        self.tab5.layout = QVBoxLayout()
        
        self.tab5.layout.addWidget(self.chooseCurrencyButton)
        self.tab5.layout.addWidget(self.issueButton)
        self.tab5.layout.addWidget(self.recipientNameButton)
        self.tab5.layout.addWidget(self.amountButton)
        self.tab5.layout.addWidget(self.issueToAccountButton) 
        self.getActionsButton.clicked.connect(self.getActions)
        self.tab5.layout.addWidget(self.transferToAccountButton)
        self.tab5.setLayout(self.tab5.layout)
        
        self.tab6.layout = QVBoxLayout() 
        #self.tab6.layout.addWidget(self.testFunctionButton)
        self.tab6.layout.addWidget(self.setPermissionObjectButton)
        self.tab6.layout.addWidget(self.testEncryptionButton)
        self.tab6.setLayout(self.tab6.layout)
        
        self.layout.addWidget(self.tabs)
        
        
        self.scrollArea = QScrollArea()
        self.layout.addWidget(self.scrollArea)
        self.scrollAreaWidgetContents = self.tabs
        self.scrollArea.setGeometry(QtCore.QRect(3000, 3000, 3000, 3000))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        
       

    def showDialog(self):
        
        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')
        
        if ok:
            self.le.setText(str(text))
            

    def slotChanged(self, newState):
        if newState == QProcess.NotRunning:
            self.startBtn.setDisabled(False)
        elif newState == QProcess.Running:
            self.startBtn.setDisabled(True)

    def startNodeos(self):
        self.start("/usr/local/eosio/bin/nodeos", ['--delete-all-blocks'])
        
    
    def readStdOutput(self):
        self.edit.append(str(self.readAllStandardOutput()))


    def createPermissionObject(self, actor, permission):
        permissionobject = {'actor':actor,'permission':permission}
        return permissionobject
        
    def setPermissionObject(self):
        self.createTestAccounts()
        actors = ['partner11111','partner22222','partner33333']
        multiSigPermissionObject = json.dumps(self.createMultiSigAccountObject(2,1, actors,'active'))
        self.account.name = 'mymultisig11'        
        subprocess.check_output(['/usr/local/eosio/bin/cleos', 'set', 'account', 'permission', self.account.name, 'active', multiSigPermissionObject, 'owner', '-p', self.account.name +'@owner',]) 
        #cleos set account permission mymultisig11 owner 
        #'{"threshold":2,"keys":[],"accounts":[{"permission":{"actor":"partner11111","permission":"owner"},"weight":1},{"permission":{"actor":"partner22222","permission":"owner"},"weight":1},{"permission":{"actor":"partner33333","permission":"owner"},"weight":1}],"waits":[]}' 
        #-p mymultisig11@owner
        multiSigPermissionObject = json.dumps(self.createMultiSigAccountObject(2,1, actors,'owner'))
        self.account.name = 'mymultisig11'        
        out = subprocess.check_output(['/usr/local/eosio/bin/cleos', 'set', 'account', 'permission', self.account.name, 'owner', multiSigPermissionObject, '-p', self.account.name +'@owner',])
        self.getInfoLabel.setText(out)
               
    def createPermissionObjectPK(self, threshold, weight):
        token1 = '{"threshold":"'
        token2 = threshold
        token3 = '","keys":[{"key":"'
        token4 = self.wallet.activePublicKey
        token5 = '","weight":"'
        token6 = weight
        token7 = '"}'
        finalToken = token1 + token2 + token3 + token4 + token5 + token6 + token7
        print(finalToken)
        return finalToken
    
    def setOwnerPermission(self):
        out = subprocess.check_output(['/usr/local/eosio/bin/cleos', 'set', 'account', 'permission', self.account.name, self.account.creator, self.wallet.activePublicKey, '-p', self.account.name, '@', self.account.creator])
        self.getInfoLabel.setText(out)
    def stakeBandwidth(self):
        out = subprocess.check_output(['/usr/local/eosio/bin/cleos', '--url', self.blockchain.producer, 'system', 'delegatebw', self.account.creator, self.account.name, self.order.stakeBandWidth, self.order.stakeCPU])
        self.getInfoLabel.setText(out)
    
    def testEncryption(self):
        key = ''
        text, ok = QInputDialog.getText(self, "QInputDialog.getText()",
                "Enter private Key:", QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            key = text
        child = pexpect.spawn(['seccure-key'])
        child.expect('Enter private key:') 
        child.sendline(key)
        child.expect(pexpect.EOF)
        out = child.before
        self.getInfoLabel.setText(out)
        child.close()
        
    
    
    def createEosioTokenAccount(self):
        self.wallet.name = 'eosio.token'
        self.createWallet()
        self.setOwnerKey()
        self.setActiveKey()
        self.importKeys()
        subprocess.check_output(['/usr/local/eosio/bin/cleos', 'create', 'account', 'eosio', 'eosio.token', self.wallet.ownerPublicKey, self.wallet.activePublicKey])   
        #cleos create account eosio eosio.token EOS7ijWCBmoXBi3CgtK7DJxentZZeTkeUnaSDvyro9dq7Sd1C3dC4 EOS7ijWCBmoXBi3CgtK7DJxentZZeTkeUnaSDvyro9dq7Sd1C3dC4
    
    
    def createEosioWallet(self):
       
        self.wallet.name = 'eosio'
        self.createWallet()
        self.setOwnerKey()
        self.setActiveKey()
        self.showKeys()
        #self.importKeys()
        subprocess.check_output(['/usr/local/eosio/bin/cleos', 'wallet', 'import', '-n', 'eosio', '--private-key', '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3'])   
        self.account.name = 'eosio'
        out = self.createAccount()   
        self.getInfoLabel.setText(out)

    def loadEosioContract(self):
        #cleos set contract eosio build/contracts/eosio.bios -p eosio
        out = subprocess.check_output(['/usr/local/eosio/bin/cleos','set', 'contract', 'eosio', os.environ['EOS_SOURCE'] + '/build/contracts/eosio.bios', '-p', 'eosio@active'])   
        self.getInfoLabel.setText(out)
    
    def showKeys(self):
        out = subprocess.check_output(['/usr/local/eosio/bin/cleos','wallet', 'keys']) 
        self.getInfoLabel.setText(out)
    
    def update_label(self):
        self.walletNameLabel.setText('Wallet Name: ' + self.wallet.name)
        self.accountNameLabel.setText('Account Name: ' + self.account.name)
        self.creatorNameLabel.setText('Creator Account Name: ' + self.account.creator)
        self.contractNameLabel.setText('Contract name: ' + self.order.contract)
        self.toggleLocalNet.setChecked(self.blockchain.running)
        if self.blockchain.running:
            self.toggleMainNet.setChecked(False)
            self.toggleTestNet.setChecked(False)
        self.blockchain.producer = self.producerBox.currentText()
        self.blockchain.testProducer = self.testProducerBox.currentText()
        
       
    def getActions(self):
        out = subprocess.check_output(['/usr/local/eosio/bin/cleos','get', 'actions', self.account.name])   
        self.getInfoLabel.setText(out)
        
    
    def lockWallet(self):
        if self.wallet.locked == False:
            subprocess.check_output(['/usr/local/eosio/bin/cleos','wallet', 'lock','-n', self.wallet.name])
            self.wallet.locked = True
            self.listWallets()
        else:
            text, ok = QInputDialog.getText(self, "QInputDialog.getText()", "Wallet Password:", QLineEdit.Normal, QtCore.QDir.home().dirName())
            if ok and text != '':
               print('')
            child = pexpect.spawn('/usr/local/eosio/bin/cleos', ['wallet', 'unlock', '-n', self.wallet.name])
            child.expect('password:') 
            child.sendline(text)
            child.expect(pexpect.EOF)
            child.close()
            self.listWallets()
            self.wallet.locked = False
        
    def stopChain(self):    
        try:
            subprocess.check_output(['killall','/usr/local/eosio/bin/nodeos'])
            self.getInfoLabel.setText('Chain stopped')
            self.blockchain.running = False
        except:
            self.getInfoLabel.setText('No chain running')
            self.blockchain.running = False
           
     
    def startChain(self):
        
        self.startNodeos()
        self.readStdOutput()
        self.getInfoLabel.setText('chain started')
        self.blockchain.running = True
        self.blockchain.net = 'local'
       
          
    def resetChain(self):
        out = ''
        try:
            out = subprocess.check_output(['rm', '-rf', os.environ['EOS_NODEOS'] + 'data'])          
        except:
            print('Already reset')
        print(os.environ['EOS_NODEOS'] + 'data')
        self.blockchain.running = False   
        self.getInfoLabel.setText('Chain reset' + str(out))
        self.account.reset()
        self.wallet.reset()
        self.order.reset()
        
    def setWalletName(self):
        text, ok = QInputDialog.getText(self, "QInputDialog.getText()",
                "Wallet name:", QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            self.wallet.name = text
            self.getInfoLabel.setText(text)
    def openWalletName(self):
        text, ok = QInputDialog.getText(self, "QInputDialog.getText()",
                "Wallet name:", QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            out = subprocess.check_output(['/usr/local/eosio/bin/cleos','wallet', 'open', '-n', text])
            self.getInfoLabel.setText(out)
    
    def setWalletPublicKeys(self):
        out = 'Owner Public Key: ' + '\n' + self.wallet.ownerPublicKey + '\n'  + 'Active Public Key: ' + '\n' + self.wallet.activePublicKey + '\n' + 'Creator Key: ' + '\n' + self.account.creatorActiveKey 
        self.getInfoLabel.setText(out)
    
    def createWallet(self):
        walletDir = os.environ['HOME'] + '/eosio-wallet'
        if not os.path.exists(walletDir):
            os.makedirs(walletDir)
        if self.blockchain.net == 'test' or self.blockchain.net == 'main':
            out = subprocess.check_output(['/usr/local/eosio/bin/cleos','-u', '"' + str(self.blockchain.producer) + '"' ,'wallet', 'create', '-n', self.wallet.name])
        else:
            out = subprocess.check_output(['/usr/local/eosio/bin/cleos','wallet', 'create', '-n', self.wallet.name])
        f = open( self.wallet.name, 'w' )
        f.write(out)
        f.close()
        line = subprocess.check_output(['tail', '-1', self.wallet.name])
        line = line.replace('"', '')
        f = open( self.wallet.name, 'w' )
        f.write(line)
        f.close()
        self.wallet.key = line
        self.wallet.locked = False
        cwd = os.getcwd()
        text = ' saved to ' + cwd
        self.getInfoLabel.setText('wallet key ' + text)
         
    

    def setOwnerKey(self):    
        out = subprocess.check_output(['/usr/local/eosio/bin/cleos', 'create', 'key'])
        key = out[13:]
        key = key[:-67]
        key2 = out[77:]
        key2 = key2[:-1]
        self.wallet.ownerPrivateKey= key
        self.wallet.ownerPublicKey = key2
        self.getInfoLabel.setText('Creating owner keys')
       

    def setActiveKey(self):
        out = subprocess.check_output(['/usr/local/eosio/bin/cleos', 'create', 'key'])
        key = out[13:]
        key = key[:-67]
        key2 = out[77:]
        key2 = key2[:-1]
        self.wallet.activePrivateKey = key
        self.wallet.activePublicKey = key2
        self.getInfoLabel.setText('Creating active keys')
        
    def importKeys(self):
        subprocess.check_output(['/usr/local/eosio/bin/cleos', 'wallet', 'import', '-n', self.wallet.name, '--private-key', self.wallet.ownerPrivateKey])
        subprocess.check_output(['/usr/local/eosio/bin/cleos', 'wallet', 'import', '-n', self.wallet.name, '--private-key', self.wallet.activePrivateKey])
        self.wallet.ownerPrivateKey = ''
        self.wallet.activePrivateKey = ''
        self.getInfoLabel.setText('Imported keys to wallet')
        
    def setAccountOwner(self):
        text, ok = QInputDialog.getText(self, "QInputDialog.getText()",
                "Account owner:", QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            self.account.owner = text
            self.getInfoLabel.setText(text)
        
         
    def createAccountName(self):
        text, ok = QInputDialog.getText(self, "QInputDialog.getText()",
                "Account name:", QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            self.account.name = text
            self.getInfoLabel.setText(text)
            
    def createCreatorAccountName(self):
        text, ok = QInputDialog.getText(self, "QInputDialog.getText()",
                "Creator name:", QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            self.account.creator = text
            self.getInfoLabel.setText(text)
        
        
    def createAccount(self):
        out = ''
        if self.blockchain.net == 'local':
            out = subprocess.check_output(['/usr/local/eosio/bin/cleos', 'create', 'account', 'eosio', self.account.name, self.wallet.ownerPublicKey, self.wallet.activePublicKey, '-p', 'eosio' ])
        elif self.blockchain.net == 'test' or self.blockchain.net == 'main': 
            permission = self.account.creator + '@active'
            out = subprocess.check_output(['/usr/local/eosio/bin/cleos', '-u', self.blockchain.producer, 'system', 'newaccount', self.account.creator, self.account.name, self.wallet.ownerPublicKey , self.wallet.activePublicKey, '--stake-net', self.order.stakeBandWidth, '--stake-cpu', self.order.stakeCPU, '--buy-ram-kbytes', self.order.buyRam, '--transfer', '-p', permission])
        self.getInfoLabel.setText(out)
    
    def LoadContract(self):
        options = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        directory = QFileDialog.getExistingDirectory(self, "Load Contract", self.getInfoLabel.text(), options)
        self.order.contract = directory
        self.order.contractAccountName = os.path.basename(directory)
        self.getInfoLabel.setText(directory)
        
    def setContractSteps(self):
        out = ''
        if self.blockchain.net == 'local':
            out = subprocess.check_output(['/usr/local/eosio/bin/cleos', 'set', 'contract', self.account.name,  self.order.contract, '-p', self.account.name ])
        elif self.blockchain.net == 'test' or self.blockchain.net == 'main': 
            out = subprocess.check_output(['/usr/local/eosio/bin/cleos', '-u', self.blockchain.producer, 'set', 'contract', self.account.name, self.order.contract, '-p', self.account.name])
        self.getInfoLabel.setText(out)
        
    def chooseCurrency(self):
        text, ok = QInputDialog.getText(self, "QInputDialog.getText()",
                "Token name:", QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            self.order.currency = text
            self.getInfoLabel.setText(text)
 
    def issueCurrency(self):
        token1 = '{"issuer": "'
        token2 = self.account.name
        token3 = '", "maximum_supply": "1000000.0000 '
        token4 = self.order.currency
        token5 = '", "can_freeze": 1, "can_recall": 1, "can_whitelist": 1}'
        finalToken = token1 + token2 + token3 + token4 + token5
        print(finalToken)
        out = subprocess.check_output(['/usr/local/eosio/bin/cleos', 'push', 'action', self.account.name, 'create', finalToken, '-p', self.account.name + '@active']) 
        self.getInfoLabel.setText(out)
    
    def setRecipientName(self):
        text, ok = QInputDialog.getText(self, "QInputDialog.getText()",
                "Recipient name:", QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            self.order.name = text
            self.getInfoLabel.setText(text)
    
    def setRecipientAccount(self):
        text, ok = QInputDialog.getText(self, "QInputDialog.getText()",
                "Recipient name:", QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            self.account.receiver = text
            self.getInfoLabel.setText(text)
    
    def setAmount(self):
        text, ok = QInputDialog.getText(self, "QInputDialog.getText()",
                "Currency Amount:", QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            self.order.amount = text 
            self.getInfoLabel.setText(self.order.amount)
    
    def setSendAmount(self):
        text, ok = QInputDialog.getText(self, "QInputDialog.getText()",
                "Currency Amount:", QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            self.order.amount = text 
            self.getInfoLabel.setText(self.order.amount)
            
    def setStakeCPUAmount(self):
        text, ok = QInputDialog.getText(self, "QInputDialog.getText()",
                "CPU Amount:", QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            self.order.stakeCPU = text 
            self.getInfoLabel.setText(self.order.stakeCPU)
            
    def setStakeBandWidthAmount(self):
        text, ok = QInputDialog.getText(self, "QInputDialog.getText()",
                "BandWith Amount:", QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            self.order.stakeBandWidth = text 
            self.getInfoLabel.setText(self.order.stakeBandWidth)
            
    def setBuyRAMAmount(self):
        text, ok = QInputDialog.getText(self, "QInputDialog.getText()",
                "Ram Amount:", QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            self.order.buyRam = text 
            self.getInfoLabel.setText(self.order.buyRam)
    
    def buyRAM(self):       
    #cleos system buyram payer receiver tokens
        out = subprocess.check_output(['/usr/local/eosio/bin/cleos', '-u', self.blockchain.producer, 'system', 'buyram', self.account.name, self.account.receiver, self.order.buyRam])
        self.getInfoLabel.setText(out)
    
    
    
    def issueToAccount(self):
        #cleos push action eosio.token issue '[ "user", "100.0000 SYS", "memo" ]' -p eosio
        token1 = '[ "'
        token2 = self.order.name
        token3 = '", "'
        token4 = self.order.amount
        token5 = '", "memo"]'
        finalToken = token1 + token2 + token3 + str(token4) + token5
        out = subprocess.check_output(['/usr/local/eosio/bin/cleos', 'push', 'action', self.account.name, 'issue', finalToken, '-p', self.account.name]) # + '@active']) 
        self.getInfoLabel.setText(out)
        
    def transferToAccount(self):
        token1 = '{"to": "'
        token2 = self.order.name
        token3 = '", "quantity": "'
        token4 = self.order.amount
        token5 = '", "memo": "testing"}'
        finalToken = token1 + token2 + token3 + str(token4) + token5
        if self.blockchain.net == 'local':
            out = subprocess.check_output(['/usr/local/eosio/bin/cleos', 'push', 'action', self.account.name, 'transfer', finalToken, '-p', self.account.name]) 
        elif self.blockchain.net == 'test' or self.blockchain.net == 'main': 
            out = subprocess.check_output(['/usr/local/eosio/bin/cleos', '-u', self.blockchain.producer, 'push', 'action', self.account.name, 'transfer', finalToken, '-p', self.account.name ])
        self.getInfoLabel.setText(out)
   
    def sendToAccount(self):
        out = ''
        if self.blockchain.net == 'local':
            out = subprocess.check_output(['/usr/local/eosio/bin/cleos', 'transfer', self.account.name, self.account.receiver, self.order.amount]) 
        elif self.blockchain.net == 'test' or self.blockchain.net == 'main': 
            out = subprocess.check_output(['/usr/local/eosio/bin/cleos', '-u', self.blockchain.producer, 'transfer', self.account.name, self.account.receiver, self.order.amount])
        self.getInfoLabel.setText(out)
    def flushWallets(self):
        text, ok = QInputDialog.getText(self, "QInputDialog.getText()",
                "save wallets to:", QLineEdit.Normal,
                '')
        if ok and text != '':
            subprocess.check_output(['mv', os.environ['HOME'] + '/eosio-wallet/', os.environ['HOME'] + "/" + text])
            self.getInfoLabel.setText("Moved Wallets"+ os.environ['HOME'] + "/" + text) 
        elif ok and text == '':
            rand = random.randint(1,1000000)
            subprocess.check_output(['mv', os.environ['HOME'] + '/eosio-wallet/', os.environ['HOME'] + '/eosio-wallet.save' + str(rand) ]) 
            self.getInfoLabel.setText("Moved Wallets"+ os.environ['HOME'] + "/" + '~/eosio-wallet.save' + str(rand))       
        subprocess.check_output(['killall', 'keosd'])
    def getInfo(self):
        out = subprocess.check_output(['/usr/local/eosio/bin/cleos', 'get', 'info'])
        self.getInfoLabel.setText(out)
        
    def getAccountDetails(self):    
        out = ''
        if self.blockchain.net == 'local':
            out = subprocess.check_output(['/usr/local/eosio/bin/cleos', 'get', 'account', self.account.name ])
        elif self.blockchain.net == 'main' :
            out = subprocess.check_output(['/usr/local/eosio/bin/cleos', '--url', self.blockchain.producer, 'get', 'account', self.account.name ])
        self.getInfoLabel.setText(out)   
        
    
    def getBalance(self):   
        out = ''
        if self.blockchain.net == 'local':
            out = subprocess.check_output(['/usr/local/eosio/bin/cleos', 'get', 'currency', 'balance', 'eosio.token', self.account.name, self.order.currency ])
        elif self.blockchain.net == 'main' :
            out = subprocess.check_output(['/usr/local/eosio/bin/cleos', '--url', self.blockchain.producer, 'get', 'currency', 'balance', 'eosio.token', self.account.name, self.order.currency ])       
        self.getInfoLabel.setText(out)    
    
    def listWallets(self):
        out = subprocess.check_output(['/usr/local/eosio/bin/cleos', 'wallet', 'list'])
        self.getInfoLabel.setText(str(out))
        
    def setBlockNumber(self):
        itext, ok = QInputDialog.getText(this, 'Input Dialog', 'Enter your name:')
        if ok:
            self.le.setText(str(text))
        #text, okPressed = QInputDialog.getText("Get text","Your name:", QLineEdit.Normal, "")
        #if okPressed and text != '':
            #print(text)
        
    def getBlockInfo(self):    
        out = subprocess.check_output(['/usr/local/eosio/bin/cleos', 'get', 'block', self.blockchain.block.number])
        self.getInfoLabel.setText(out)
        
    def listProducers(self):
        out = ''
        if self.blockchain.net == 'test':
            producerConv = 'https://' + self.blockchain.testProducer
            print(producerConv)
            out = subprocess.check_output(['/usr/local/eosio/bin/cleos', '--url', 'https://dc1.eosemerge.io:5443' , 'system', 'listproducers'])
        elif self.blockchain.net == 'main' :
            producerConv = self.blockchain.producer
            print(producerConv)
            out = subprocess.check_output(['/usr/local/eosio/bin/cleos', '--url', 'https://dc1.eosemerge.io:5443', 'system', 'listproducers'])
        self.getInfoLabel.setText(out)    
     
    def getProducerInfo(self): 
        out = ''
        if self.blockchain.net == 'test':
            producerConv = 'https://' + self.blockchain.testProducer
            print(producerConv)
            out = subprocess.check_output(['/usr/local/eosio/bin/cleos', '--url', 'https://dc1.eosemerge.io:5443', 'get', 'info'])
            self.getInfoLabel.setText(self.blockchain.producer + '\n' + out)   
        elif self.blockchain.net == 'main' :
            out = subprocess.check_output(['/usr/local/eosio/bin/cleos', '--url', self.blockchain.producer, 'get', 'info'])
            self.getInfoLabel.setText(self.blockchain.producer + '\n' + out)   
    def mainNet(self):
        if self.toggleMainNet.checkState() != 0:
            self.stopChain()
            self.resetChain()
            self.blockchain.net = 'main'
            self.blockchain.running = False
            self.toggleTestNet.setChecked(False)
            self.toggleLocalNet.setChecked(False)
            self.getInfoLabel.setText('Switched to main net')
        else:
            self.getInfoLabel.setText("Off the main net")
            #self.blockchain.running = False
    def localNet(self):
        if self.toggleLocalNet.checkState() != 0:
            self.stopChain()
            self.resetChain()
            self.startChain()
            self.blockchain.net = 'local'
            self.blockchain.running = True
            self.getInfoLabel.setText('Switched to local net')
        else:
            self.blockchain.running = False
            self.stopChain()
            self.getInfoLabel.setText("Off local net")
            
    def testNet(self):
        if self.toggleTestNet.checkState() != 0:
            self.stopChain()
            self.resetChain()
            self.blockchain.running = False
            self.blockchain.net = 'test'
            self.toggleMainNet.setChecked(False)
            self.toggleLocalNet.setChecked(False)
            self.getInfoLabel.setText('Switched to test net')
        else:
            self.getInfoLabel.setText("Off test net")
    

def main():
   
        
    app = QApplication(sys.argv)
    qProcess = GUI()
    qProcess.setProcessChannelMode(QProcess.MergedChannels)
    qProcess.readyReadStandardOutput.connect(qProcess.readStdOutput)
    return app.exec_()


if __name__ == '__main__':
    main()
