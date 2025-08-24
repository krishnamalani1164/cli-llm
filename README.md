# NL→CLI: Natural Language to Command Line Interface

A security-focused tool that translates natural language queries into Linux CLI commands for sysadmins and cybersecurity professionals.

## 🎯 Target Users
- **System Administrators** - streamline daily operations
- **Cybersecurity Students** - learn security tools through natural language

## ⚡ Core Features
- **Natural Language Translation** - convert plain English to Linux commands
- **Security Tools Support** - zenmap, hydra, snort, bandit, and more
- **Suggest-Only Mode** - all commands require user confirmation before execution
- **Ambiguity Handling** - multiple ranked suggestions when queries are unclear
- **Modular Architecture** - easily extensible for new tools and platforms

## 🛡 Safety & Access Control
- **Role-Based Safety** - different permission levels for beginners vs experts
- **GUI Access Manager** - administrators control user access and permissions
- **No Auto-Execution** - commands are suggested, never run automatically

## 🖥 Platform Support
- **Primary**: Linux (all major distributions)
- **Future**: Cross-platform extensibility planned

## 🧠 Technology Stack
- **Model**: Fine-tuned open-source LLM
- **Training Data**: Curated natural language → CLI command pairs
- **Interface**: CLI for end users, GUI for access management

## 🚀 Version 1.0 Scope
Focus on core NL→CLI translation functionality:
- ✅ Natural language query processing
- ✅ Command suggestion generation
- ✅ User confirmation workflow
- ✅ Basic security tool coverage
- ⏳ Advanced explainability features (future versions)
- ⏳ Script generation capabilities (future versions)

## 📊 Evaluation Metrics
- **Accuracy** - correct command translation rate
- **Safety** - prevention of harmful command execution
- **Usability** - user satisfaction and workflow efficiency

## Getting Started
```bash
# Installation and usage instructions coming soon
nlcli "scan this network for open ports"
# → Suggests: nmap -sS 192.168.1.0/24
# → Confirm execution? [y/N]
```

## Contributing
This project is in active development. Contribution guidelines and development setup instructions will be available soon.
