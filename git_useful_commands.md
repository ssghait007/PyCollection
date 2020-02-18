# git log decorative
git log --oneline --graph --decorate --all
# git rebase commands
git checkout feature
git rebase master
- if git rebase gives conflict you can abort or resolve conflicts and continue the rebase
git rebase --abort
resolve conflicts and
git rebase --continue
# git tagging
git tag appVersion1
git tag -a v-0.9-beta commitid // tagging particular commit
git tag --list
git tag --delete appVersion1
git tag -a v-1.0 // asks for message
git show v-1.0 // shows extra info(tag name, tagger, date , message)
git diff tag1 tag2
git tag -a v-0.8 -f commitid // force update
- push tags to git
  git push origin tagName
  git push origin master --tags
  git push origin :tagName // tag gets deleted from remote 
# stash commands
git stash 
git stash save 'changes'
git stash apply stash{i}
git stash show stash{i}
git stash drop stash{i}
git stash clear
git stash pop
- stash untracked and modified 
git stash -u 
- apply these into a new branch
git stash branch newchanges
# git reset and reflog and cherry pick
git reset HEAD^ // removes last commit
git reset HEAD^i // removes last i commits
git reflog // log of everything
git reset commitid // reset to that commit just like timr travel
git reset HEAD{i} 
git cherry-pick commitid // commitid from another branch